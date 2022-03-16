from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from user.models import Black, Pick
from user.serializers import BlackCreateSerializer, PickCreateSerializer, BlackReadSerializer, PickReadSerializer


class BlackCreateViewSet(ModelViewSet):
    queryset = Black.objects.all()
    serializer_class = BlackCreateSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]


class BlackReadViewSet(ModelViewSet):
    queryset = Black.objects.all()

    def get_serializer_class(self):
        method = self.request.method
        if method == "PUT" or method == "POST" or method == "PATCH":
            return BlackCreateSerializer
        else:
            return BlackReadSerializer


class PickCreateViewSet(ModelViewSet):
    queryset = Pick.objects.all()
    serializer_class = PickCreateSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]


class PickReadViewSet(ModelViewSet):
    queryset = Pick.objects.all()

    def get_serializer_class(self):
        method = self.request.method
        if method == "PUT" or method == "POST" or method == "PATCH":
            return PickCreateSerializer
        else:
            return PickReadSerializer
