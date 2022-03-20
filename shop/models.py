from django.core.validators import RegexValidator, MinLengthValidator
from django.db import models
from accounts.models import User


class Shop(models.Model):
    shop_num = models.CharField(max_length=10, db_index=True, unique=True, validators=[
        MinLengthValidator(10),
        RegexValidator(regex='^[0-9]*$', message="숫자만 입력해주세요"),
    ],)
    name = models.CharField(max_length=100, db_index=True)
    category = models.CharField(max_length=100, db_index=True)
    address = models.CharField(max_length=300)
    lat = models.FloatField(default=0)
    longitude = models.FloatField(default=0)
    telephone = models.CharField(max_length=12,  validators=[
             RegexValidator(r"^\d{3,4}\d{3,4}\d{4}$",
                            message="전화번호를 입력해 주세요."),
         ], help_text="입력 예) 0421112222")
    opening_hours = models.TextField(blank=True)
    holiday = models.CharField(max_length=1, default="0")
    now_table_count = models.IntegerField(default=0)
    total_table_count = models.IntegerField(default=0)
    conv_parking = models.BooleanField(default=False)
    conv_pet = models.BooleanField(default=False)
    conv_wifi = models.BooleanField(default=False)
    conv_pack = models.BooleanField(default=False)
    notice = models.TextField(blank=True)
    intro = models.TextField(blank=True)
    wait_state = models.CharField(max_length=1, default="0")
    photo1 = models.ImageField(blank=True, upload_to='media/%Y/%m/%d')
    photo2 = models.ImageField(blank=True, upload_to='media/%Y/%m/%d')
    photo3 = models.ImageField(blank=True, upload_to='media/%Y/%m/%d')
    registered_date = models.DateTimeField(auto_now_add=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)






