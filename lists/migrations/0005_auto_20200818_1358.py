# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-08-18 12:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0004_auto_20200817_2224'),
    ]

    operations = [
        migrations.AddField(
            model_name='pd',
            name='adress',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='pd',
            name='email',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='pd',
            name='phone_number',
            field=models.TextField(default=''),
        ),
    ]
