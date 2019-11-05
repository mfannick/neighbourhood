# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-11-05 14:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('neighbourapp', '0010_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='businessLocation',
            field=models.CharField(choices=[('Amahoro', 'Amahoro'), ('Agaciro', 'Agaciro'), ('Intsinzi', 'Intsinzi')], default=django.utils.timezone.now, max_length=60),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='neighbour',
            name='neighbourName',
            field=models.CharField(choices=[('Amahoro', 'Amahoro'), ('Agaciro', 'Agaciro'), ('Intsinzi', 'Intsinzi')], max_length=60),
        ),
    ]
