# Generated by Django 5.0.4 on 2024-04-08 08:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultation', '0044_delete_paymentt'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookings',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='consultation.users'),
        ),
    ]
