# Generated by Django 3.0 on 2024-03-15 17:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consultation', '0028_auto_20240315_1034'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='order',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='product',
        ),
        migrations.RenameField(
            model_name='cart',
            old_name='items',
            new_name='products',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='OrderItem',
        ),
    ]
