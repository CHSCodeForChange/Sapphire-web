# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-24 00:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utility', '0029_auto_20180321_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slot',
            name='address',
            field=models.CharField(max_length=240, null=True),
        ),
        migrations.AlterField(
            model_name='slot',
            name='city',
            field=models.CharField(max_length=240, null=True),
        ),
        migrations.AlterField(
            model_name='slot',
            name='description',
            field=models.CharField(max_length=960, null=True),
        ),
        migrations.AlterField(
            model_name='slot',
            name='location',
            field=models.CharField(max_length=240, null=True),
        ),
        migrations.AlterField(
            model_name='slot',
            name='state',
            field=models.CharField(max_length=2, null=True),
        ),
    ]