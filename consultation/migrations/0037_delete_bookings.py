# Generated by Django 3.2.22 on 2024-04-05 09:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consultation', '0036_bookings_room'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Bookings',
        ),
    ]