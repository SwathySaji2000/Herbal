# Generated by Django 3.0 on 2024-04-01 05:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('consultation', '0029_auto_20240315_2251'),
    ]

    operations = [
        migrations.CreateModel(
            name='P_booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_amount', models.CharField(max_length=2000, null=True)),
                ('p_date', models.CharField(max_length=2000, null=True)),
                ('p_status', models.CharField(max_length=225, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consultation.Users')),
            ],
        ),
        migrations.CreateModel(
            name='P_bookingchild',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_amount', models.CharField(max_length=225)),
                ('quantity', models.CharField(max_length=225)),
                ('P_booking_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consultation.P_booking')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consultation.Product')),
            ],
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='cart',
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='product',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='CartItem',
        ),
    ]