from rest_framework import serializers
from waiting.models import Waiting


class WaitingCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Waiting
        fields = "__all__"


class WaitingReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Waiting
        fields = "__all__"
        depth = 1
