# Generated by Django 3.2.12 on 2022-03-17 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('waiting', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='waiting',
            name='wait_date',
            field=models.DateTimeField(),
        ),
    ]