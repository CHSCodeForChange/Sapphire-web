# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-01 04:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('utility', '0017_auto_20180130_2337'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_slot',
            old_name='volunteers',
            new_name='volunteer',
        ),
    ]
