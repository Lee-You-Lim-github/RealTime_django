# Generated by Django 3.2.12 on 2022-03-18 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shop',
            old_name='photo',
            new_name='photo1',
        ),
        migrations.AddField(
            model_name='shop',
            name='photo2',
            field=models.ImageField(blank=True, upload_to='media/%Y/%m/%d'),
        ),
        migrations.AddField(
            model_name='shop',
            name='photo3',
            field=models.ImageField(blank=True, upload_to='media/%Y/%m/%d'),
        ),
    ]
