# Generated by Django 3.0.6 on 2020-07-05 17:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_user_hourlyrate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 5, 19, 33, 11, 297394)),
        ),
    ]