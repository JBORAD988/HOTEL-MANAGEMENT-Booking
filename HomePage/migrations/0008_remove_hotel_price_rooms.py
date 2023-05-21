# Generated by Django 4.0.3 on 2022-05-31 08:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HomePage', '0007_alter_hotel_host'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotel',
            name='price',
        ),
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_type', models.CharField(choices=[('1', 'premium'), ('2', 'deluxe'), ('3', 'basic')], max_length=50)),
                ('capacity', models.IntegerField()),
                ('price', models.IntegerField()),
                ('size', models.IntegerField()),
                ('status', models.CharField(choices=[('1', 'available'), ('2', 'not available')], max_length=15)),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HomePage.hotel')),
            ],
        ),
    ]
