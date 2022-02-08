from django.contrib.auth.hashers import make_password
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(models.Model):
    user_id = models.CharField(max_length=60, db_index=True, unique=True)
    password = models.CharField(_('password'), max_length=128)
    name = models.CharField(max_length=60, db_index=True)
    nickname = models.CharField(max_length=60, unique=True)
    telephone = models.CharField(max_length=12, validators=[
             RegexValidator(r"^\d{3}\d{4}\d{4}$",
                            message="전화번호를 입력해 주세요."),
         ], db_index=True)
    authority = models.CharField(max_length=1, default=0)
    signup_date = models.DateTimeField(auto_now_add=True)

    _password = None

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
        self._password = raw_password