from rest_framework import serializers
from booking.serializers import BookingListSerializer
from review.serializers import ReviewSerializer
from shop.models import Shop


class ShopCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = "__all__"


class ShopListSerializer(serializers.ModelSerializer):
    booking_set = BookingListSerializer(many=True, read_only=True)
    review_set = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Shop
        fields = "__all__"
        depth = 1











