# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-26 09:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LinkAct', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='friend_movement',
            field=models.CharField(default='[]', max_length=300),
        ),
        migrations.AddField(
            model_name='myuser',
            name='movement_link',
            field=models.CharField(default='[]', max_length=300),
        ),
        migrations.AddField(
            model_name='myuser',
            name='movement_name',
            field=models.CharField(default='[]', max_length=300),
        ),
    ]