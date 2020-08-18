# Generated by Django 3.0.6 on 2020-07-28 14:41

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0028_auto_20200721_2052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 28, 14, 41, 35, 590203, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 28, 14, 41, 35, 593668)),
        ),
        migrations.AlterField(
            model_name='user',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 28, 14, 41, 35, 586382, tzinfo=utc)),
        ),
        migrations.CreateModel(
            name='Balance_transactions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requested_on', models.DateTimeField(auto_now_add=True)),
                ('done_on', models.DateTimeField(blank=True, null=True)),
                ('amount', models.FloatField(default=0.0)),
                ('pending', models.BooleanField(default=True)),
                ('refused', models.BooleanField(default=False)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
