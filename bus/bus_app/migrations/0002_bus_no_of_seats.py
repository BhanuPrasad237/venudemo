# Generated by Django 5.2.1 on 2025-05-12 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bus_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bus',
            name='no_of_seats',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]
