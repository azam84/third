# Generated by Django 3.1.4 on 2020-12-07 08:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car_app', '0006_auto_20201207_1102'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car_information',
            name='engine',
        ),
        migrations.RemoveField(
            model_name='car_information',
            name='gearbox',
        ),
        migrations.RemoveField(
            model_name='car_information',
            name='year',
        ),
    ]