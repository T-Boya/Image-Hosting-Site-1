# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2018-05-23 13:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0014_photo_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='Location',
        ),
        migrations.AddField(
            model_name='photo',
            name='location',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='rango.Location'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='location',
            name='title',
            field=models.CharField(blank=True, max_length=128),
        ),
    ]
