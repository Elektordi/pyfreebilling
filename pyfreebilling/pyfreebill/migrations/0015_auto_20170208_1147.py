# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-02-08 10:47
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import pyfreebilling.pyfreebill.models


class Migration(migrations.Migration):

    dependencies = [
        ('pyfreebill', '0014_auto_20170109_1942'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customerrates',
            name='date_end',
        ),
        migrations.RemoveField(
            model_name='customerrates',
            name='date_start',
        ),
        migrations.RemoveField(
            model_name='providerrates',
            name='date_end',
        ),
        migrations.RemoveField(
            model_name='providerrates',
            name='date_start',
        ),
        migrations.AddField(
            model_name='customerrates',
            name='destnum_length',
            field=models.IntegerField(default=0, help_text='If value > 0, then destination number must match tsi length', verbose_name='Destination number length'),
        ),
        migrations.AddField(
            model_name='ratecard',
            name='date_end',
            field=models.DateTimeField(default=pyfreebilling.pyfreebill.models.default_time),
        ),
        migrations.AddField(
            model_name='ratecard',
            name='date_start',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 8, 10, 47, 19, 856828, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='carriercidnormalizationrules',
            name='prefix',
            field=models.CharField(max_length=30, verbose_name='prefix'),
        ),
        migrations.AlterField(
            model_name='carriernormalizationrules',
            name='prefix',
            field=models.CharField(max_length=30, verbose_name='prefix'),
        ),
        migrations.AlterField(
            model_name='customercidnormalizationrules',
            name='prefix',
            field=models.CharField(max_length=30, verbose_name='prefix'),
        ),
    ]
