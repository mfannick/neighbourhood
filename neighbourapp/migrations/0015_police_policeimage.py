# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-11-05 17:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('neighbourapp', '0014_police_policelocation'),
    ]

    operations = [
        migrations.AddField(
            model_name='police',
            name='policeImage',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='police/'),
            preserve_default=False,
        ),
    ]