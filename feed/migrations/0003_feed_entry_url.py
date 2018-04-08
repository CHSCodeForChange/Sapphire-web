# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-22 19:57
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0002_feed_entry_datetime'),
    ]

    operations = [
        migrations.AddField(
            model_name='feed_entry',
            name='url',
            field=models.CharField(default=datetime.datetime(2018, 1, 22, 19, 57, 29, 601605, tzinfo=utc), max_length=120),
            preserve_default=False,
        ),
    ]
