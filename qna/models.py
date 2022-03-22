from django.db import models
from accounts.models import User


class Qna(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    answer = models.TextField(null=True, blank=True)
    photo = models.ImageField(null=True, blank=True)
    registered_date = models.DateField(auto_now_add=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

