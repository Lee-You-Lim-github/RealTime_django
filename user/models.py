from datetime import timedelta
from django.db import models
from django.utils import timezone
from accounts.models import User
from booking.models import Booking
from shop.models import Shop


now = timezone.now()


def default_date():
    return now + timedelta(days=1)


def default_end_date():
    return default_date() + timedelta(days=3)


class Black(models.Model):
    start_date = models.DateField(default=default_date)
    end_date = models.DateField(default=default_end_date)
    black_count = models.CharField(max_length=1, default="0")
    book_id = models.ForeignKey(Booking, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)


class Pick(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    shop_id = models.ForeignKey(Shop, on_delete=models.CASCADE)
