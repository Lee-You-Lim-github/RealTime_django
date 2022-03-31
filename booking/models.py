from django.core.exceptions import ValidationError
from django.db import models
from shop.models import Shop
from accounts.models import User


class Booking(models.Model):

    class VisitStatusChoices(models.TextChoices):
        TO_VISIT = "0", "방문 예정"
        VISITED = "1", "방문"
        NO_SHOW = "2", "미방문"

    class BookMethod(models.TextChoices):
        NOW_BOOK = "0", "지금예약"
        NO_NOW_BOOK = "1", "지금말고 예약"


    day = models.DateField()
    time = models.TimeField()
    book_table_count = models.IntegerField(default=0)
    visit_status = models.CharField(max_length=1,
                                    choices=VisitStatusChoices.choices,
                                    default=VisitStatusChoices.TO_VISIT)
    method = models.CharField(max_length=1, choices=BookMethod.choices)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    shop_id = models.ForeignKey(Shop, on_delete=models.CASCADE)

    # def save(self, *args, **kwargs):
    #     if self.day < date.today():
    #         raise ValidationError("지난 날짜는 예약할 수 없습니다.")
    #
    #     if self.time < datetime.today().time():
    #         raise ValidationError("지난 시간은 예약할 수 없습니다.")
    #     super(Booking, self).save(*args, **kwargs)

    # class Meta:
    #     ordering = ['day']
    #
    # def save(self, *args, **kwargs):
    #
    #     recent_booking = Booking.objects.filter(
    #         user_id_id = self.black_set[0].user_id.id
    #     )
    #
    #     if recent_booking:
    #         self.book_table_count = recent_booking.book_table_count + 1
    #     else:
    #         self.book_table_count = 1
    #
    #     super(Booking, self).save(*args, **kwargs)