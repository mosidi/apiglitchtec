# Generated by Django 3.0.6 on 2020-07-21 03:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0022_auto_20200721_0342'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='Resumate',
            field=models.FileField(blank=True, null=True, upload_to='media'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 21, 3, 47, 8, 111067)),
        ),
        migrations.AlterField(
            model_name='user',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 21, 3, 47, 8, 105478, tzinfo=utc)),
        ),
    ]
