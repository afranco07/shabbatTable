# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-01 04:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frijay', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='accept',
            field=models.NullBooleanField(default=None),
        ),
    ]
