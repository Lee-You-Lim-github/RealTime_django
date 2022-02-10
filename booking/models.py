from django.db import models
from shop.models import Shop
from accounts.models import User


class Booking(models.Model):
    day = models.DateField()
    time = models.TimeField()
    book_table_count = models.IntegerField(default=0)
    visit_status = models.CharField(max_length=1)
    method = models.CharField(max_length=1)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    shop_num = models.ForeignKey(Shop, on_delete=models.CASCADE)