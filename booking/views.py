from django.shortcuts import render
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from booking.models import Booking
from booking.serializers import BookingSerializer


class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]

    # def get_queryset(self):
    #     qs= super().get_queryset()
    #
    #     query=self.request.query_params.get("query","")
    #     if query:
    #         qs=qs.filter(champion__icontains=query)
    #
    #     return qs



