from django.db import models
from accounts.models import User
from booking.models import Booking
from shop.models import Shop


class Black(models.Model):
    black_date = models.CharField(max_length=1)
    book_id = models.ForeignKey(Booking, on_delete=models.CASCADE)


class Pick(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    shop_id = models.ForeignKey(Shop, on_delete=models.CASCADE)
