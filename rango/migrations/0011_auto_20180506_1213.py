# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2018-05-06 09:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0010_auto_20180506_1212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='location',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='rango.Location'),
        ),
    ]
