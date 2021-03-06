# Generated by Django 3.2.12 on 2022-03-16 16:20

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('booking', '0001_initial'),
        ('waiting', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveSmallIntegerField(default=5, validators=[django.core.validators.MaxValueValidator(5)])),
                ('content', models.CharField(max_length=150)),
                ('flavor', models.CharField(choices=[('매우좋아요', '매우좋아요'), ('좋아요', '좋아요'), ('보통이에요', '보통이에요'), ('별로예요', '별로예요'), ('싫어요', '싫어요')], max_length=20)),
                ('cleaned', models.CharField(choices=[('매우좋아요', '매우좋아요'), ('좋아요', '좋아요'), ('보통이에요', '보통이에요'), ('별로예요', '별로예요'), ('싫어요', '싫어요')], max_length=20)),
                ('kindness', models.CharField(choices=[('매우좋아요', '매우좋아요'), ('좋아요', '좋아요'), ('보통이에요', '보통이에요'), ('별로예요', '별로예요'), ('싫어요', '싫어요')], max_length=20)),
                ('mood', models.CharField(choices=[('매우좋아요', '매우좋아요'), ('좋아요', '좋아요'), ('보통이에요', '보통이에요'), ('별로예요', '별로예요'), ('싫어요', '싫어요')], max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('book_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='booking.booking')),
                ('wait_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='waiting.waiting')),
            ],
        ),
    ]
