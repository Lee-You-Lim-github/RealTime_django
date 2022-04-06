from datetime import timedelta
from django.db import models
from django.utils import timezone
from accounts.models import User
from booking.models import Booking
from shop.models import Shop


def default_date():
    now = timezone.now()
    return now + timedelta(days=1)


def default_end_date():
    now = timezone.now()
    return now + timedelta(days=3)


class Black(models.Model):
    start_date = models.DateField(default=default_date)
    end_date = models.DateField(default=default_end_date)
    black_count = models.CharField(max_length=1, default="0")
    book_id = models.ForeignKey(Booking, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super(Black, self).save(*args, **kwargs)

        if self.black_count != "0":
            BlackLog.objects.create(start_date=self.start_date, end_date=self.end_date,
                                    black_count=self.black_count, black_id=self,
                                    book_id=self.book_id, user_id=self.user_id)


class BlackLog(models.Model):
    start_date = models.DateField(default=default_date)
    end_date = models.DateField(default=default_end_date)
    black_count = models.CharField(max_length=1, default="0")
    black_id = models.ForeignKey(Black, on_delete=models.SET_NULL, null=True)
    book_id = models.ForeignKey(Booking, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)


class Pick(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    shop_id = models.ForeignKey(Shop, on_delete=models.CASCADE)
