# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-14 00:06
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('utility', '0004_event_is_single'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='address',
            field=models.CharField(default='address', max_length=240),
        ),
        migrations.AddField(
            model_name='event',
            name='state',
            field=models.CharField(default=datetime.datetime(2018, 1, 14, 0, 6, 7, 119340, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='zip_code',
            field=models.IntegerField(null=True),
        ),
    ]
