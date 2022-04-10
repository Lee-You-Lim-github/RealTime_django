from typing import Dict

from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework_simplejwt.serializers import (
    TokenObtainPairSerializer as OriginTokenObtainPairSerializer,
    TokenRefreshSerializer as OriginTokenRefreshSerializer,
)

from booking.serializers import BookingListSerializer
from user.serializers import BlackSerializer, BlackLogSerializer

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    booking_set = BookingListSerializer(many=True, read_only=True)
    black_set = BlackSerializer(many=True, read_only=True)
    blacklog_set = BlackLogSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ["id", "user_id", "username", "nickname", "telephone", "authority", "date_joined", "is_superuser", "is_active", "shop_set", "booking_set", "black_set", "blacklog_set"]

        # def update(self, instance, validated_data):


class UserCreationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ["user_id", "username", "password", "password2", "nickname", "telephone", "authority"]

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError("동일한 암호를 지정해주세요.")
        return attrs



    def create(self, validated_data):
        user_id = validated_data["user_id"]
        username = validated_data["username"]
        password = validated_data["password"]
        nickname = validated_data["nickname"]
        telephone = validated_data["telephone"]
        authority = validated_data["authority"]

        new_user = User(user_id=user_id, username=username, nickname=nickname, telephone=telephone, authority=authority)
        new_user.set_password(password)
        new_user.save()

        return new_user


class TokenObtainPairSerializer(OriginTokenObtainPairSerializer):
    def validate(self, attrs):
        data: Dict = super().validate(attrs)
        data["id"] = self.user.id
        data["user_id"] = self.user.user_id
        data["username"] = self.user.username
        data["nickname"] = self.user.nickname
        data["telephone"] = self.user.telephone
        data["authority"] = self.user.authority
        data["is_superuser"] = self.user.is_superuser
        return data


class TokenRefreshSerializer(OriginTokenRefreshSerializer):
    pass


