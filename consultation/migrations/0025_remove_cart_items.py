# Generated by Django 3.0 on 2024-03-15 05:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consultation', '0024_cart_items'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='items',
        ),
    ]
