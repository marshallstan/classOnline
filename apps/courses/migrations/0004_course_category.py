# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-21 22:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20190320_0805'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='category',
            field=models.CharField(default='IT程序员', max_length=20, verbose_name='课程类别'),
        ),
    ]
