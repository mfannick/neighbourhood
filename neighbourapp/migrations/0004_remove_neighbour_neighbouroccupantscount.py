# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-11-01 09:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('neighbourapp', '0003_auto_20191101_0911'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='neighbour',
            name='neighbourOccupantsCount',
        ),
    ]
