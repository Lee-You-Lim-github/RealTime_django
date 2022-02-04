from django.db import models

from shop.models import Shop
from user.models import User


class Booking(models.Model):
    book_num = models.AutoField(primary_key=True)
    day = models.DateField()
    time = models.DateTimeField()
    table_count = models.IntegerField(default=0)
    visit_status = models.CharField(max_length=1)
    method = models.CharField(max_length=1)
    id = models.ForeignKey(User, on_delete=models.CASCADE)
    shop_num = models.ForeignKey(Shop, on_delete=models.CASCADE)
