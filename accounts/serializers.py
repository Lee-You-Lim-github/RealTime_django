from typing import Dict

from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework_simplejwt.serializers import (
    TokenObtainPairSerializer as OriginTokenObtainPairSerializer,
    TokenRefreshSerializer as OriginTokenRefreshSerializer,
)

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["user_id", "username", "nickname", "telephone", "authority"]


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
            raise serializers.ValidationError("Difference between passwords")
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
        data["user_id"] = self.user.user_id
        data["authority"] = self.user.authority

        return data


class TokenRefreshSerializer(OriginTokenRefreshSerializer):
    pass