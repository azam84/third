# Generated by Django 3.1.4 on 2020-12-07 08:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('car_app', '0007_auto_20201207_1201'),
    ]

    operations = [
        migrations.AddField(
            model_name='car_information',
            name='year',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='car_app.modelyear'),
        ),
    ]