# Generated by Django 3.2.12 on 2022-03-31 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_alter_booking_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='method',
            field=models.CharField(choices=[('0', '지금예약'), ('1', '지금말고 예약')], max_length=1),
        ),
        migrations.AlterField(
            model_name='booking',
            name='visit_status',
            field=models.CharField(choices=[('0', '방문 예정'), ('1', '방문'), ('2', '미방문')], default='0', max_length=1),
        ),
    ]
