# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-08-17 21:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0003_pd'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pd',
            name='adress',
        ),
        migrations.RemoveField(
            model_name='pd',
            name='email',
        ),
        migrations.RemoveField(
            model_name='pd',
            name='phone_number',
        ),
    ]
