from rest_framework import serializers
from shop.models import Shop, Conv, Review


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = "__all__"


class ConvSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conv
        fields = "__all__"


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"