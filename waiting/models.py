from django.db import models
from accounts.models import User
from shop.models import Shop


class Waiting(models.Model):
    wait_count = models.IntegerField(default=0)
    wait_date = models.DateTimeField()
    wait_table_count = models.IntegerField(default=0)
    wait_visit_status = models.CharField(max_length=1, default="0")
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    shop_id = models.ForeignKey(Shop, on_delete=models.CASCADE)

    class Meta:
        ordering = ['wait_date']