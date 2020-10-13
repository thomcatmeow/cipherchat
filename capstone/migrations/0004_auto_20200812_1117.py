# Generated by Django 3.0.8 on 2020-08-12 16:17

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capstone', '0003_auto_20200812_1115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='members',
            field=models.ManyToManyField(blank=True, default=None, related_name='members', to=settings.AUTH_USER_MODEL),
        ),
    ]
