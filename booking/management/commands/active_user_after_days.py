import datetime
from django.core.management import BaseCommand
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
        # black_count가 1일때
        black_qs_today_count_1 = Black.objects.all().filter(
            end_date__lte=datetime.datetime.today(),
            black_count="1",
        )
        print("블랙1", black_qs_today_count_1)

        # black_count가 2일때
        black_qs_today_count_2 = Black.objects.all().filter(
            end_date__lte=datetime.datetime.today(),
            black_count="2",
        )
        print("블랙2", black_qs_today_count_2)

        # black_count가 3일때
        black_qs_today_count_3 = Black.objects.all().filter(
            end_date__lte=datetime.datetime.today(),
            black_count="3",
        )
        print("블랙3:", black_qs_today_count_3)

        if black_qs_today_count_3.exists():
            updated = user_qs.filter(black__in=black_qs_today_count_3).update(is_active=True)
            print("updated", updated)
            delete = black_qs_today_count_3.delete()
            print("delete", delete)

        elif black_qs_today_count_2.exists():
            updated = user_qs.filter(black__in=black_qs_today_count_2).update(is_active=True)
            print("블랙2: updated", updated)
            delete = black_qs_today_count_2.delete()
            print("블랙2: delete", delete)

        elif black_qs_today_count_1.exists():
            updated = user_qs.filter(black__in=black_qs_today_count_1).update(is_active=True)
            print("블랙1: updated", updated)
            delete = black_qs_today_count_1.delete()
            print("블랙1: delete", delete)

        else:
            print("블랙유저가 없습니다.")
