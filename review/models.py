from django.core.validators import MaxValueValidator
from django.db import models
from booking.models import Booking
from waiting.models import Waiting


class Review(models.Model):

    CHOICES = (
        ("매우좋아요", "매우좋아요"),
        ("좋아요", "좋아요"),
        ("보통이에요", "보통이에요"),
        ("별로예요", "별로예요"),
        ("싫어요", "싫어요"),
    )
    rating = models.PositiveSmallIntegerField(
        validators=[MaxValueValidator(5)],
        default=5)
    content = models.CharField(max_length=150)
    flavor = models.CharField(max_length=20, choices=CHOICES)
    cleaned = models.CharField(max_length=20, choices=CHOICES)
    kindness = models.CharField(max_length=20, choices=CHOICES)
    mood = models.CharField(max_length=20, choices=CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    book_id = models.ForeignKey(Booking, null=True, on_delete=models.CASCADE)
    wait_id = models.ForeignKey(Waiting, null=True, on_delete=models.CASCADE)
