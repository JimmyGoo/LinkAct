# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-28 08:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LinkAct', '0009_interest_linked_theme'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='friend_movement_id',
            field=models.CharField(default='[]', max_length=300),
        ),
    ]
