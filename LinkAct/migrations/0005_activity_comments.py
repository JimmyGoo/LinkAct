# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-27 10:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LinkAct', '0004_activity_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='comments',
            field=models.CharField(default='[]', max_length=300),
        ),
    ]
