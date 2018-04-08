# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-31 04:32
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('utility', '0015_auto_20180130_2326'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_Slot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('signin', models.DateTimeField()),
                ('signout', models.DateTimeField()),
                ('volunteers', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='slot',
            name='signin',
        ),
        migrations.RemoveField(
            model_name='slot',
            name='signout',
        ),
        migrations.RemoveField(
            model_name='slot',
            name='volunteers',
        ),
        migrations.AddField(
            model_name='slot',
            name='user_slots',
            field=models.ManyToManyField(to='utility.User_Slot'),
        ),
    ]
