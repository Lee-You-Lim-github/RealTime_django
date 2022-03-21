from django.db import models
from accounts.models import User


class Qna(models.Model):
    qna_title = models.CharField(max_length=100)
    qna_content = models.TextField()
    qna_answer = models.TextField(null=True, blank=True)
    qna_photo = models.TextField(null=True, blank=True)
    qna_registered_date = models.DateField(auto_now_add=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

