from django.db import models
from accounts.models import User
from shop.models import Shop
from django.utils import timezone


class Waiting(models.Model):
    wait_count = models.IntegerField(default=1)
    wait_date = models.DateTimeField(auto_now_add=True)
    wait_table_count = models.IntegerField(default=0)
    wait_visit_status = models.CharField(max_length=1, default="0")
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    shop_id = models.ForeignKey(Shop, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-wait_date']

    def save(self, *args, **kwargs):
        now = timezone.now()

        recent_waiting = Waiting.objects.filter(
            wait_date__date=now.date(),
            shop_id=self.shop_id).order_by("-wait_date").first()

        if recent_waiting:
            self.wait_count = recent_waiting.wait_count + 1
        else:
            self.wait_count = 1

        super(Waiting, self).save(*args, **kwargs)
