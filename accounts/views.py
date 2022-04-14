from django.contrib.auth import get_user_model
from rest_framework import viewsets, status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView as OriginTokenObtainPairView,
    TokenRefreshView as OriginTokenRefreshView,
)

from accounts.paginations.UserPagination import UserPagination
from accounts.serializers import (
    TokenObtainPairSerializer,
    UserCreationSerializer,
    UserSerializer,
)
from django.db.models import Q
from accounts.naver_sms import send_sms

from user.models import Black

Account = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = UserSerializer
    pagination_class = UserPagination
    permission_classes = [AllowAny]  # DRF 디폴트 설정

    def get_queryset(self):
        qs = super().get_queryset()

        query = self.request.query_params.get("query", "")
        black = self.request.query_params.get("black", "")
        id = self.request.query_params.get("id", "")
        user_id = self.request.query_params.get("user_id", "")
        conditions = Q(username__icontains=query) | Q(telephone__icontains=query)
        id_conditions = Q(id__exact=id)
        user_id_conditions = Q(user_id__exact=user_id)
        black_conditions = Q(black__isnull=True)

        if query:
            qs = qs.filter(conditions | Q(user_id__icontains=query))

        if id:
            qs = qs.filter(id_conditions)

        if user_id:
            qs = qs.filter(user_id_conditions)

        if black:
            qs = qs.exclude(black_conditions)

        return qs


class SignupAPIView(CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = UserCreationSerializer
    permission_classes = [AllowAny]


class TokenObtainPairView(OriginTokenObtainPairView):
    serializer_class = TokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        userId = request.data["user_id"]
        user = Account.objects.get(user_id=userId)
        black = Black.objects.filter(user_id_id__exact=user.id).first()

        if not user.is_active:
            if black.black_count == "4":
                message = "영구 정지된 회원입니다."
            else:
                message = f"""{black.start_date}부터 {black.end_date}까지 활동이 정지되었습니다."""

            return Response(
                {
                    "detail": "블랙",
                    "message": f"""{message}\n(주)지금어때 공식페이지를 통해서 문의해주세요.\n(주)지금어때는 건강한 예약문화를 추구합니다.""",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        return super().post(request, *args, **kwargs)


class TokenRefreshView(OriginTokenRefreshView):
    pass


class NaverSmsApi(APIView):
    def post(self, request):
        data = request.data
        message = data["messages"][0]["content"]
        phone_number = data["messages"][0]["to"]
        send_sms(phone_number, message)

        return Response(data)
