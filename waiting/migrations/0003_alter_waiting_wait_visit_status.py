# Generated by Django 3.2.12 on 2022-03-21 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('waiting', '0002_alter_waiting_wait_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='waiting',
            name='wait_visit_status',
            field=models.CharField(default='0', max_length=1),
        ),
    ]
