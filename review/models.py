from django.core.validators import MaxValueValidator
from django.db import models
from booking.models import Booking
from waiting.models import Waiting


class Review(models.Model):
    class Choices(models.TextChoices):
        VERY_GOOD = ("매우좋아요", "매우좋아요")
        GOOD = ("좋아요", "좋아요")
        NORMAL = ("보통이에요", "보통이에요")
        BAD = ("별로예요", "별로예요")
        VERY_BAD = ("싫어요", "싫어요")

    rating = models.PositiveSmallIntegerField(
        validators=[MaxValueValidator(5)],
        default=5)
    content = models.CharField(max_length=150)
    flavor = models.CharField(max_length=20,  choices=Choices.choices)
    cleaned = models.CharField(max_length=20, choices=Choices.choices)
    kindness = models.CharField(max_length=20, choices=Choices.choices)
    mood = models.CharField(max_length=20, choices=Choices.choices)
    created_at = models.DateTimeField(auto_now_add=True)
    book_id = models.ForeignKey(Booking, null=True, blank=True, on_delete=models.CASCADE)
    wait_id = models.ForeignKey(Waiting, null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created_at']
