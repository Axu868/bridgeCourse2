# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-08-18 23:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0005_auto_20200818_1358'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(default='')),
            ],
        ),
    ]
