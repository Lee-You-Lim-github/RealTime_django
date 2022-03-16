from django.db import models
from accounts.models import User


class Qna(models.Model):
    qna_title = models.CharField(max_length=100)
    qna_content = models.TextField()
    qna_answer = models.TextField()
    qna_photo = models.TextField()
    qna_registered_date = models.DateField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

