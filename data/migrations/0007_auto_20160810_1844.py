# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-11 01:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0006_auto_20160806_1822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contributor',
            name='individual',
            field=models.ForeignKey(blank=True, help_text='Individual who contributed this donation. Only for class 1 donations.', null=True, on_delete=django.db.models.deletion.CASCADE, to='data.ContributorIndividual'),
        ),
        migrations.AlterField(
            model_name='contributor',
            name='organization',
            field=models.ForeignKey(blank=True, help_text='Organization that contributed this donation.', null=True, on_delete=django.db.models.deletion.CASCADE, to='data.ContributorOrganization'),
        ),
        migrations.AlterField(
            model_name='donation',
            name='amount',
            field=models.FloatField(help_text='Size of the donation in dollars', verbose_name='Amount'),
        ),
        migrations.AlterField(
            model_name='filer',
            name='affiliation',
            field=models.CharField(choices=[('BC LIBERAL PARTY', 'Liberal'), ('BC NDP', 'NDP'), ('BC CONSERVATIVE PARTY', 'Conservative')], max_length=40),
        ),
        migrations.AlterField(
            model_name='filer',
            name='name',
            field=models.CharField(help_text='Name of the person who reported the donation.', max_length=200),
        ),
    ]