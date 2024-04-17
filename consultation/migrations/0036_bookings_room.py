# Generated by Django 3.2.22 on 2024-04-05 05:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('consultation', '0035_auto_20240405_1038'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('room_type', models.CharField(choices=[('ac', 'AC'), ('non_ac', 'Non-AC')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Bookings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_start', models.DateField()),
                ('date_end', models.DateField()),
                ('treatment_type', models.CharField(choices=[('panchakarma', 'Panchakarma'), ('massage', 'Massage'), ('meditation', 'Meditation'), ('yoga', 'Yoga')], max_length=100)),
                ('food_plan', models.CharField(choices=[('regular', 'Regular'), ('vegetarian', 'Vegetarian'), ('vegan', 'Vegan'), ('gluten_free', 'Gluten-Free')], max_length=100)),
                ('number_of_days', models.PositiveIntegerField(choices=[(3, '3 days'), (5, '5 days'), (7, '7 days')])),
                ('status', models.CharField(default='pending', max_length=100)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consultation.room')),
            ],
        ),
    ]
