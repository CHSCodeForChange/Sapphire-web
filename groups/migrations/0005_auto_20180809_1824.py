# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-08-09 22:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0004_auto_20180809_1811'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='eventName',
        ),
        migrations.RemoveField(
            model_name='group',
            name='slotName',
        ),
    ]
