# Generated by Django 3.0 on 2024-02-17 07:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consultation', '0003_prescription'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prescription',
            name='user_id',
        ),
    ]