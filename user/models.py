from django.core.validators import RegexValidator
from django.db import models


class User(models.Model):
    id = models.CharField(max_length=60, db_index=True, primary_key=True)
    password = models.CharField(max_length=20)
    password2 = models.CharField(max_length=20)
    name = models.CharField(max_length=60, db_index=True)
    nickname = models.CharField(max_length=60, unique=True)
    telephone = models.CharField(max_length=12, validators=[
             RegexValidator(r"^\d{3}\d{4}\d{4}$",
                            message="전화번호를 입력해 주세요."),
         ], db_index=True)
    authority = models.CharField(max_length=1, default=0)
    signup_date = models.DateTimeField(auto_now_add=True)

