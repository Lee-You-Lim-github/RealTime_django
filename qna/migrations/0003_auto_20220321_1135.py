# Generated by Django 3.2.12 on 2022-03-21 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qna', '0002_auto_20220318_2113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qna',
            name='qna_photo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='qna',
            name='qna_registered_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]