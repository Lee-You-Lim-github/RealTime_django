from rest_framework import serializers
from booking.models import Booking


class BookingCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"

class BookingReadserializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"
        depth = 1

