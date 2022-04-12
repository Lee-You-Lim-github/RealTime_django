import datetime

from rest_framework import serializers

from accounts.models import User
from booking.models import Booking
from review.serializers import ReviewSerializer
from user.models import Black, BlackLog
from user.serializers import BlackSerializer


class BookingCreateSerializer(serializers.ModelSerializer):
    black_set = BlackSerializer(many=True, required=False, allow_null=True)

    class Meta:
        model = Booking
        fields = "__all__"

    def create(self, validated_data):
        if "black_set" in self.validated_data:
            _ = validated_data.pop('black_set')
            booking = Booking.objects.create(**validated_data)

            request = self.context.get("request")
            black_datas = request.data.get("black_set")

            for black_data in black_datas:
                for key, value in black_data.items():
                    user = User.objects.get(id__exact=value)
                    Black.objects.create(book_id=booking, user_id=user)

            return booking

        else:
            booking = Booking.objects.create(**validated_data)

            return booking

    def update(self, instance, validated_data):
        visit_status = validated_data.get("visit_status")
        black_log_list = BlackLog.objects.filter(user_id__exact=instance.user_id)
        day_7 = datetime.datetime.today() + datetime.timedelta(days=7)
        day_30 = datetime.datetime.today() + datetime.timedelta(days=30)

        if visit_status == "2":

            if black_log_list.count() >= 4:
                account = User.objects.get(user_id=instance.user_id)
                account.is_active = False
                account.save()
            else:
                black = Black.objects.create(book_id=instance, user_id=instance.user_id)

                black.black_count = black_log_list.count() + 1
                account = User.objects.get(user_id=instance.user_id)
                account.is_active = False
                account.save()

                if black_log_list.count() == 1:
                    black.end_date = day_7
                    account = User.objects.get(user_id=instance.user_id)
                    account.is_active = False
                    account.save()

                if black_log_list.count() == 2:
                    black.end_date = day_30
                    account = User.objects.get(user_id=instance.user_id)
                    account.is_active = False
                    account.save()

                if black_log_list.count() == 3:
                    account = User.objects.get(user_id=instance.user_id)
                    account.is_active = False
                    account.save()

                black.save()

        instance.visit_status = visit_status
        instance.save()
        return instance


class BookingListSerializer(serializers.ModelSerializer):
    review_set = ReviewSerializer(many=True, read_only=True)
    black_set = BlackSerializer(many=True, required=False, allow_null=True)

    class Meta:
        model = Booking
        fields = "__all__"
        depth = 1

