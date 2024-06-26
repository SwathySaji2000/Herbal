# Generated by Django 3.0 on 2024-03-15 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultation', '0027_auto_20240315_1034'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='items',
            field=models.ManyToManyField(through='consultation.CartItem', to='consultation.Product'),
        ),
        migrations.AddField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(through='consultation.OrderItem', to='consultation.Product'),
        ),
    ]
