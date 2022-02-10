from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.core.validators import RegexValidator, MinLengthValidator


class CustomUserManager(UserManager):
    def create_user(self, user_id, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        if not user_id:
            raise ValueError('Users must have an user_id')

        user = self.model(
            user_id=user_id,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, user_id, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        user = self.create_user(
            user_id,
            password=password,
            **extra_fields
        )

        user.is_admin = True
        user.save(using=self._db)

        return user


class User(AbstractUser):
    USERNAME_FIELD = 'user_id'
    REQUIRED_FIELDS = []

    first_name = None
    last_name = None
    last_login = None
    email = None

    user_id = models.CharField(max_length=20, unique=True, validators=[
        MinLengthValidator(3),
        RegexValidator(regex='^[a-zA-Z0-9]*$', message="영문/숫자를 혼합하여 입력해주세요"),
    ], )
    username = models.CharField(max_length=60, db_index=True, validators=[
        RegexValidator(regex='^[ㄱ-힣]*$', message="한글만 입력해주세요"),
    ], )
    nickname = models.CharField(max_length=15, unique=True, validators=[
        RegexValidator(regex='^[ㄱ-힣]*$', message="한글만 입력해주세요"),
    ])
    telephone = models.CharField(max_length=12, validators=[
        RegexValidator(r"^\d{3}\d{4}\d{4}$",
                       message="전화번호를 입력해 주세요."),
    ], help_text="입력 예) 01011112222", db_index=True)
    authority = models.CharField(max_length=1, default=0)

    objects = CustomUserManager()


