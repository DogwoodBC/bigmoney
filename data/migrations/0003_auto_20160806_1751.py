# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-07 00:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_auto_20160806_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filer',
            name='type',
            field=models.CharField(choices=[('CANDIDATE', 'candidate'), ('CONSTITUENCY', 'constituency'), ('ASSOCIATION', 'association'), ('POLITICAL PARTY', 'political party')], max_length=30),
        ),
    ]
