# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-07 01:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0003_auto_20160806_1751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filer',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]