from rest_framework import serializers
from shop.models import Shop, Review


class ShopCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = [
            "id", "shop_num", "name", "category", "address", "lat", "long", "telephone", "opening_hours", "now_table_count",
            "total_table_count", "conv_parking", "conv_pet", "conv_wifi", "conv_pack", "notice", "intro", "photo", "registered_date", "user_id"
        ]


class ShopReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = "__all__"
        depth = 1


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"







