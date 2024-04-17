# Generated by Django 3.0 on 2024-02-27 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultation', '0011_product_usage_instructions'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='certifications',
            field=models.ImageField(default=True, max_length=1000, upload_to=''),
        ),
        migrations.AddField(
            model_name='product',
            name='expiry_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='manufacturer',
            field=models.ImageField(max_length=2000, null=True, upload_to=''),
        ),
    ]