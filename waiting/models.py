from django.db import models
from accounts.models import User
from shop.models import Shop
from django.utils import timezone


class Waiting(models.Model):
    class VisitStatusChoices(models.TextChoices):
        WAITING = "0", "대기 중"
        ENTRY = "1", "입장"
        NO_SHOW = "2", "미입장"

    class CancelChoices(models.TextChoices):
        NO_CANCEL = "0", "취소아님"
        CANCEL = "1", "취소됨"

    wait_count = models.IntegerField(default=1)
    wait_date = models.DateTimeField(auto_now_add=True)
    wait_table_count = models.IntegerField(default=0)
    wait_visit_status = models.CharField(max_length=1,
                                         choices=VisitStatusChoices.choices,
                                         default=VisitStatusChoices.WAITING)
    wait_cancel = models.CharField(max_length=1,
                                   choices=CancelChoices.choices,
                                   default=CancelChoices.NO_CANCEL)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    shop_id = models.ForeignKey(Shop, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-wait_date']

    @property
    def is_cancel(self) -> bool:
        return self.wait_cancel == self.CancelChoices.CANCEL

    @property
    def is_wait_status(self):
        return self.wait_visit_status == self.VisitStatusChoices.WAITING

    def save(self, *args, **kwargs):
        now = timezone.now()

        if not self.is_cancel and self.is_wait_status:
            recent_waiting = Waiting.objects.filter(
                wait_date__date=now.date(),
                shop_id=self.shop_id).order_by("-wait_date").first()

            if recent_waiting:
                self.wait_count = recent_waiting.wait_count + 1
            else:
                self.wait_count = 1

        super(Waiting, self).save(*args, **kwargs)
