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
