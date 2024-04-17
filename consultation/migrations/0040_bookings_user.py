# Generated by Django 5.0.4 on 2024-04-09 16:12

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultation', '0039_remove_bookings_date_end'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookings',
            name='user',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, to='consultation.users'),
            preserve_default=False,
        ),
    ]