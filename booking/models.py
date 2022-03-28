from django.core.exceptions import ValidationError
from django.db import models
from shop.models import Shop
from accounts.models import User
from datetime import date
from datetime import datetime


class Booking(models.Model):
    day = models.DateField()
    time = models.TimeField()
    book_table_count = models.IntegerField(default=0)
    visit_status = models.CharField(max_length=1)
    method = models.CharField(max_length=1)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    shop_id = models.ForeignKey(Shop, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if self.day < date.today():
            raise ValidationError("지난 날짜는 예약할 수 없습니다.")

        if self.time < datetime.today().time():
            raise ValidationError("지난 시간은 예약할 수 없습니다.")
        super(Booking, self).save(*args, **kwargs)

    class Meta:
        ordering = ['day']