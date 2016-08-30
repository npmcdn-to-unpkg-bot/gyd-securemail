# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-30 18:41
from __future__ import unicode_literals

from django.db import migrations, models
import securemsg.models


class Migration(migrations.Migration):

    dependencies = [
        ('securemsg', '0003_auto_20160830_1825'),
    ]

    operations = [
        migrations.AddField(
            model_name='datarequest',
            name='slug',
            field=models.SlugField(default=securemsg.models.randomString),
        ),
        migrations.AlterField(
            model_name='publickey',
            name='email_address',
            field=models.EmailField(max_length=254),
        ),
    ]