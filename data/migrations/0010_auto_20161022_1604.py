# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-22 23:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0009_auto_20161022_1541'),
    ]

    operations = [
        migrations.AddField(
            model_name='uniqueindividual',
            name='name_first_middle',
            field=models.CharField(default='', help_text='First and any middle parts of the name provided.', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='uniqueindividual',
            name='name_last',
            field=models.CharField(default='', help_text='Last part of the name provided.', max_length=100),
            preserve_default=False,
        ),
    ]
