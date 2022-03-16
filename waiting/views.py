from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from waiting.models import Waiting
from waiting.serializers import WaitingCreateSerializer, WaitingReadSerializer


class WaitingCreateViewSet(ModelViewSet):
    queryset = Waiting.objects.all()
    serializer_class = WaitingCreateSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]


class WaitingReadViewSet(ModelViewSet):
    queryset = Waiting.objects.all()
    ordering_fields = ['wait_date']

    def get_serializer_class(self):
        method = self.request.method
        if method == "PUT" or method == "POST" or method == "PATCH":
            return WaitingCreateSerializer
        else:
            return WaitingReadSerializer


