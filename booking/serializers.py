from rest_framework import serializers
from booking.models import Booking
from review.serializers import ReviewSerializer


class BookingCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"


class BookingListSerializer(serializers.ModelSerializer):
    review_set = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Booking
        fields = "__all__"
        depth = 1

