# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-18 18:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0008_auto_20170718_2123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=250, unique=True),
        ),
    ]
