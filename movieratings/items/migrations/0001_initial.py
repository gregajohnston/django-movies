# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-11 04:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('movie_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=150)),
                ('date_added', models.DateField(verbose_name='date added')),
                ('imdb_url', models.CharField(max_length=200)),
                ('genre_1', models.CharField(default=0, max_length=50)),
                ('genre_2', models.CharField(default=0, max_length=50)),
                ('genre_3', models.CharField(default=0, max_length=50)),
                ('genre_4', models.CharField(default=0, max_length=50)),
                ('genre_5', models.CharField(default=0, max_length=50)),
                ('genre_6', models.CharField(default=0, max_length=50)),
                ('genre_7', models.CharField(default=0, max_length=50)),
                ('genre_8', models.CharField(default=0, max_length=50)),
                ('genre_9', models.CharField(default=0, max_length=50)),
                ('genre_10', models.CharField(default=0, max_length=50)),
                ('genre_11', models.CharField(default=0, max_length=50)),
                ('genre_12', models.CharField(default=0, max_length=50)),
                ('genre_13', models.CharField(default=0, max_length=50)),
                ('genre_14', models.CharField(default=0, max_length=50)),
                ('genre_15', models.CharField(default=0, max_length=50)),
                ('genre_16', models.CharField(default=0, max_length=50)),
                ('genre_17', models.CharField(default=0, max_length=50)),
                ('genre_18', models.CharField(default=0, max_length=50)),
                ('genre_19', models.CharField(default=0, max_length=50)),
                ('genre_20', models.CharField(default=0, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Rater',
            fields=[
                ('rater_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('age', models.IntegerField(default=0)),
                ('gender', models.CharField(max_length=1)),
                ('occupation', models.CharField(max_length=150)),
                ('zip_code', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_id', models.CharField(default=0, max_length=20)),
                ('rater_id', models.CharField(default=0, max_length=20)),
                ('rating', models.IntegerField(default=0)),
                ('timestamp', models.IntegerField(default=0)),
            ],
        ),
    ]
