# Generated by Django 3.2.12 on 2022-04-06 16:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import user.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('booking', '0003_auto_20220331_1602'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlackLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(default=user.models.default_date)),
                ('end_date', models.DateField(default=user.models.default_end_date)),
                ('black_count', models.CharField(default='0', max_length=1)),
                ('black_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.black')),
                ('book_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.booking')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]