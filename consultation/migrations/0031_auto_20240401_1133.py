# Generated by Django 3.0 on 2024-04-01 06:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consultation', '0030_auto_20240401_1109'),
    ]

    operations = [
        migrations.RenameField(
            model_name='p_bookingchild',
            old_name='P_booking_id',
            new_name='P_booking',
        ),
    ]