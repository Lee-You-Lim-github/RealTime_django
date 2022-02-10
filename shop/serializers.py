from rest_framework import serializers
from shop.models import Shop, Conv, Review


class ConvSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conv
        fields = "__all__"


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"


class ShopSerializer(serializers.ModelSerializer):
    shop_convs = ConvSerializer(many=True)

    class Meta:
        model = Shop
        fields = [
            "shop_num",
            "name",
            "category",
            "address",
            "lat",
            "long",
            "telephone",
            "opening_hours",
            "total_table_count",
            "now_table_count",
            "shop_convs",
            "notice",
            "intro",
            "photo",
            "registered_date",
            "user_id",
        ]

    def create(self, validated_data):
        tracks_data = validated_data.pop('tracks')
        shop_id = Shop.objects.create(**validated_data)
        for track_data in tracks_data:
            Conv.objects.create(album=shop_id, **track_data)
        return shop_id



