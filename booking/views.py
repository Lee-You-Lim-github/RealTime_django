from django.db.models import Q
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from booking.models import Booking
from booking.serializers import BookingCreateSerializer, BookingReadSerializer


class BookingCreateViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingCreateSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]


class BookingReadViewSet(ModelViewSet):
    queryset = Booking.objects.all()

    def get_serializer_class(self):
        method = self.request.method
        if method == 'PUT' or method == 'POST' or method == 'PATCH':
            return BookingCreateSerializer
        else:
            return BookingReadSerializer

    # def get_queryset(self):
    #     qs = super().get_queryset()
    #
    #     query = self.request.query_params.get("query", "")
    #     conditions = Q(username__icontains=query) | Q(telephone__icontains=query)
    #     if query:
    #         qs = qs.filter(conditions)
    #
    #     return qs




