# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-27 12:47
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LinkAct', '0006_auto_20160727_2001'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='comment_time',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
