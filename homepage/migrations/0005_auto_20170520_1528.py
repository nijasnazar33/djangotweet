# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-20 09:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0004_auto_20170520_1345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='followers',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_id',
            field=models.CharField(max_length=100),
        ),
    ]