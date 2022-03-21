from django.db.models import Q
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from user.models import Black, Pick
from user.serializers import BlackCreateSerializer, PickCreateSerializer, BlackSerializer, PickSerializer


class BlackViewSet(ModelViewSet):
    queryset = Black.objects.all()
    serializer_class = BlackSerializer

    # def get_permissions(self):
    #     if self.request.method == "GET":
    #         return [AllowAny()]
    #     return [IsAuthenticated()]

    def get_serializer_class(self):
        method = self.request.method
        if method == "PUT" or method == "POST" or method == "PATCH":
            return BlackCreateSerializer
        else:
            return BlackSerializer


class PickViewSet(ModelViewSet):
    queryset = Pick.objects.all()
    serializer_class = PickSerializer

    # def get_permissions(self):
    #     if self.request.method == "GET":
    #         return [AllowAny()]
    #     return [IsAuthenticated()]

    def get_serializer_class(self):
        method = self.request.method
        if method == "PUT" or method == "POST" or method == "PATCH":
            return PickCreateSerializer
        else:
            return PickSerializer

    def get_queryset(self):
        qs = super().get_queryset()

        user_id = self.request.query_params.get("user_id", "")
        shop_id = self.request.query_params.get("shop_id", "")
        conditions = Q(user_id_id__exact=user_id) & Q(shop_id_id__exact=shop_id)
        if user_id and shop_id:
            qs = qs.filter(conditions)

        user_id_conditions = Q(user_id__id__exact=user_id)
        if user_id:
            qs = qs.filter(user_id_conditions)

        return qs
