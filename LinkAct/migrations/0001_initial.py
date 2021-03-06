# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-26 03:45
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(default='', max_length=20)),
                ('creator', models.IntegerField()),
                ('participants', models.CharField(default='[]', max_length=300)),
                ('locale', models.CharField(default='', max_length=20)),
                ('theme', models.CharField(default='[]', max_length=300)),
                ('create_time', models.DateField(default=datetime.date.today)),
                ('start_date', models.DateField(default=datetime.date.today)),
                ('end_date', models.DateField(default=datetime.date.today)),
                ('introduction', models.CharField(default='[]', max_length=500)),
                ('supporters', models.CharField(default='[]', max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commenter', models.IntegerField()),
                ('score', models.IntegerField()),
                ('content', models.CharField(default='', max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Img',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='upload')),
            ],
        ),
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(default='', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(default='', max_length=20)),
                ('birthday', models.DateField(default=datetime.date.today)),
                ('website', models.URLField()),
                ('city', models.CharField(default='', max_length=20)),
                ('head', models.IntegerField(default=-1)),
                ('participate_terminative_acts', models.CharField(default='[]', max_length=300)),
                ('create_terminative_acts', models.CharField(default='[]', max_length=300)),
                ('participate_ongoing_acts', models.CharField(default='[]', max_length=300)),
                ('create_ongoing_acts', models.CharField(default='[]', max_length=300)),
                ('commented_acts', models.CharField(default='[]', max_length=300)),
                ('gender', models.CharField(default='', max_length=20)),
                ('interests', models.CharField(default='[]', max_length=300)),
                ('phone_number', models.CharField(default='', max_length=20)),
                ('waiting_deal_friends', models.CharField(default='[]', max_length=300)),
                ('friends', models.CharField(default='[]', max_length=300)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(default='', max_length=100)),
            ],
        ),
    ]
