# Generated by Django 5.0.3 on 2024-03-25 16:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('capacity', models.IntegerField()),
                ('poc_name', models.CharField(max_length=100)),
                ('poc_email', models.CharField(max_length=100)),
                ('image_url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('venue_type', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('door_time', models.TimeField(blank=True)),
                ('start_time', models.TimeField()),
                ('ga_price', models.IntegerField()),
                ('vip_price', models.IntegerField(blank=True)),
                ('image_url', models.URLField()),
                ('venue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='server.venue')),
            ],
        ),
    ]
