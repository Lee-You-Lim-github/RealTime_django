from rest_framework import serializers
from shop.models import Shop, Conv, Review


class ConvSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conv
        fields = ["parking", "pet", "wifi", "pack"]


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
            "user_id_id",
        ]

    def create(self, validated_data):
        shop_convs_data = validated_data.pop('shop_convs')
        shop_id = Shop.objects.create(**validated_data)
        for shop_conv_data in shop_convs_data:
            Conv.objects.create(shop_id=shop_id, **shop_conv_data)
        return shop_id



