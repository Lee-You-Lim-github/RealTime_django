import datetime

from django.core.management import BaseCommand
from django.db.models import F

from accounts.models import User
from user.models import Black


class Command(BaseCommand):
    help = '3일 지난 black유저를 활성화해줍니다.'

    def handle(self, *args, **options):

        # 개원회원이고 활성화가 안 된 회원들만 조회
        user_qs = User.objects.filter(
            authority=User.AuthorityChoices.PERSONAL,
            is_active=False
        )

        # end_date <= today인 경우만 조회
        black_qs_today = Black.objects.all().filter(end_date__lte=datetime.datetime.today())

        # black_count가 1일때
        black_count_1_qs = Black.objects.all().filter(black_count="1")

        # black_count가 2일때
        black_count_2_qs = Black.objects.all().filter(black_count="2")

        # black_count가 3일때
        black_count_3_qs = Black.objects.all().filter(black_count="3")

        if black_qs_today and black_count_1_qs:
            updated = user_qs.filter(black__in=black_qs_today).update(is_active=True)
            print("updated", updated)
            print("블랙1")

        elif black_qs_today and black_count_2_qs:
            updated = user_qs.filter(black__in=black_qs_today and black_count_2_qs).update(is_active=True)
            print("updated", updated)
            print("블랙2")

        else:
            print("실패")

        # end_date-start_date의 차이가 2일 이상인 Black만 조회
        # black_qs_6_days = Black.objects.all()\
        #     .annotate(diff = F('end_date') - F('start_date'))\
        #     .filter(diff__lte=datetime.timedelta(days=6)).exists()
        #
        # if black_qs:
        #     updated = user_qs.filter(black__in=black_qs).update(is_active=True)
        #     print("updated", updated)
        #
        # else:
        #     print("실패")