from rest_framework import serializers

from review.serializers import ReviewSerializer
from waiting.models import Waiting


class WaitingCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Waiting
        fields = "__all__"


class WaitingListSerializer(serializers.ModelSerializer):
    review_set = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Waiting
        fields = "__all__"
        depth = 1
