# Generated by Django 5.1.6 on 2025-02-16 00:03

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0005_delivery'),
    ]

    operations = [
        migrations.AddField(
            model_name='delivery',
            name='delivery_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
