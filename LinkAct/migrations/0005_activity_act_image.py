# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-27 15:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LinkAct', '0004_activity_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='act_image',
            field=models.IntegerField(default=-1),
        ),
    ]
