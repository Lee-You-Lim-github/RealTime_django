# Generated by Django 3.2.12 on 2022-03-16 14:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shop', '0003_rename_long_shop_longitude'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Waiting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wait_count', models.IntegerField(default=0)),
                ('wait_date', models.DateField()),
                ('wait_table_count', models.IntegerField(default=0)),
                ('wait_visit_status', models.CharField(max_length=1)),
                ('shop_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.shop')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['wait_date'],
            },
        ),
    ]