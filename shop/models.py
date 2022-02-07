from django.core.validators import RegexValidator
from django.db import models

from user.models import User


class Shop(models.Model):
    shop_num = models.CharField(max_length=10, db_index=True, unique=True)
    password = models.CharField(max_length=20)
    password2 = models.CharField(max_length=20)
    name = models.CharField(max_length=100, db_index=True)
    category = models.CharField(max_length=100, db_index=True)
    address = models.CharField(max_length=300)
    telephone = models.CharField(max_length=12,  validators=[
             RegexValidator(r"^\d{3,4}\d{3,4}\d{4}$",
                            message="전화번호를 입력해 주세요."),
         ])
    opening_hours = models.TextField(blank=True)
    table_count = models.IntegerField(default=0)
    notice = models.TextField(blank=True)
    intro = models.TextField(blank=True)
    photo = models.ImageField(blank=True)
    registered_date = models.DateTimeField(auto_now_add=True)


class Conv(models.Model):
    parking = models.BooleanField(default=False)
    pet = models.BooleanField(default=False)
    wifi = models.BooleanField(default=False)
    pack = models.BooleanField(default=False)
    shop_num = models.ForeignKey(Shop, on_delete=models.CASCADE)


class Review(models.Model):
    rating = models.IntegerField(default=5)
    content = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    shop_num = models.ForeignKey(Shop, on_delete=models.CASCADE)
