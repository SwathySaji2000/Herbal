# Generated by Django 3.0 on 2024-02-29 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultation', '0016_auto_20240229_2309'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_image',
            field=models.ImageField(blank=True, max_length=1000, null=True, upload_to='product_images/'),
        ),
    ]