from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView as OriginTokenObtainPairView,
    TokenRefreshView as OriginTokenRefreshView,
)

from accounts.paginations.UserPagination import UserPagination
from accounts.serializers import TokenObtainPairSerializer, UserCreationSerializer, UserSerializer
from django.db.models import Q
from accounts.naver_sms import send_sms

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = UserPagination
    permission_classes = [AllowAny]   # DRF 디폴트 설정

    def get_queryset(self):
        qs = super().get_queryset()

        query = self.request.query_params.get("query", "")
        conditions = Q(username__icontains=query) | Q(telephone__icontains=query)
        if query:
            qs = qs.filter(conditions | Q(user_id__icontains=query))

        return qs


class SignupAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreationSerializer
    permission_classes = [AllowAny]


class TokenObtainPairView(OriginTokenObtainPairView):
    serializer_class = TokenObtainPairSerializer


class TokenRefreshView(OriginTokenRefreshView):
    pass

class NaverSmsApi(APIView):

    def post(self, request):
        data = request.data
        message = data["content"]
        phone_number = data["messages"][0]["to"]
        send_sms(phone_number, message)
        print(data)
        print(message)
        print(phone_number)

        return Response(data)