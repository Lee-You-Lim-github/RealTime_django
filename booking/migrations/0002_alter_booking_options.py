# Generated by Django 3.2.12 on 2022-03-16 10:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='booking',
            options={'ordering': ['day']},
        ),
    ]
