# Generated by Django 5.1.6 on 2025-02-15 22:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0003_alter_pizza_cheese_alter_pizza_crust_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
