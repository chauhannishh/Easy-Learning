# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-11-27 18:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0017_auto_20171128_0012'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='image',
        ),
        migrations.AddField(
            model_name='category',
            name='icon_name',
            field=models.CharField(default='info', max_length=20),
        ),
    ]
