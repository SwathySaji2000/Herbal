# Generated by Django 3.0 on 2024-02-29 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultation', '0014_auto_20240228_1530'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='ayurvedic_properties',
        ),
        migrations.AlterField(
            model_name='product',
            name='manufacturer',
            field=models.CharField(max_length=2000, null=True),
        ),
    ]