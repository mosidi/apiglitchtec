# Generated by Django 3.0.6 on 2020-07-15 04:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_auto_20200711_0450'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='deivceid',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 15, 6, 42, 38, 342514)),
        ),
        migrations.AlterField(
            model_name='user',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 15, 6, 42, 38, 329547)),
        ),
    ]