# Generated by Django 3.2.12 on 2022-04-06 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='authority',
            field=models.CharField(choices=[('0', '개인 회원'), ('1', '사업자 회원')], default='0', max_length=1),
        ),
    ]
