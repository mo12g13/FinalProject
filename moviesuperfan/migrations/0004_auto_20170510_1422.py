# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-10 19:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviesuperfan', '0003_auto_20170507_1109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermovie',
            name='movie_watch',
            field=models.BooleanField(default=False),
        ),
    ]