# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-24 00:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utility', '0031_auto_20180323_1919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slot',
            name='address',
            field=models.CharField(blank=True, max_length=240, null=True),
        ),
        migrations.AlterField(
            model_name='slot',
            name='city',
            field=models.CharField(blank=True, max_length=240, null=True),
        ),
        migrations.AlterField(
            model_name='slot',
            name='description',
            field=models.CharField(blank=True, max_length=960, null=True),
        ),
        migrations.AlterField(
            model_name='slot',
            name='location',
            field=models.CharField(blank=True, max_length=240, null=True),
        ),
        migrations.AlterField(
            model_name='slot',
            name='state',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='slot',
            name='zip_code',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
