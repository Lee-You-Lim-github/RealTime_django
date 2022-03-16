from rest_framework import serializers
from booking.serializers import BookingListSerializer
from review.serializers import ReviewSerializer
from shop.models import Shop


class ShopCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = [
            "id", "shop_num", "name", "category", "address", "lat", "longitude", "telephone", "opening_hours", "holiday", "now_table_count",
            "total_table_count", "conv_parking", "conv_pet", "conv_wifi", "conv_pack", "notice", "intro", "photo", "registered_date", "user_id"
        ]


class ShopListSerializer(serializers.ModelSerializer):
    booking_set = BookingListSerializer(many=True, read_only=True)
    review_set = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Shop
        fields = "__all__"
        depth = 1











