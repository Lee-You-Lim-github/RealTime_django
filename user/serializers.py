from rest_framework import serializers
from user.models import Black, Pick, BlackLog


class BlackCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Black
        fields = "__all__"


class BlackLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlackLog
        fields = "__all__"


class BlackLogCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlackLog
        fields = "__all__"


class BlackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Black
        fields = "__all__"
        depth = 1


class PickCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pick
        fields = "__all__"


class PickSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pick
        fields = "__all__"
        depth = 1
