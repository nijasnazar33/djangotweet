# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-15 16:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tweet_id', models.IntegerField()),
                ('tweet_type', models.CharField(max_length=15)),
                ('tweet_text', models.CharField(max_length=150)),
                ('tweet_text2', models.CharField(max_length=150)),
                ('tweet_text_url', models.CharField(max_length=150)),
                ('retweets', models.IntegerField()),
                ('favourites', models.IntegerField()),
                ('created_at', models.DateField()),
            ],
        ),
        migrations.RenameModel(
            old_name='Users',
            new_name='User',
        ),
        migrations.RemoveField(
            model_name='tweets',
            name='user',
        ),
        migrations.DeleteModel(
            name='Tweets',
        ),
        migrations.AddField(
            model_name='tweet',
            name='tweet_op',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.User'),
        ),
    ]
