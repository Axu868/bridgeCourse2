# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-08-23 21:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0008_i_r'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='r',
            name='reference',
        ),
        migrations.AddField(
            model_name='r',
            name='email',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='r',
            name='name',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='r',
            name='phone',
            field=models.TextField(default=''),
        ),
    ]
