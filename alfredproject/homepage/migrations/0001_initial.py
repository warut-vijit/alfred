# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-02 22:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Balance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_from', models.PositiveSmallIntegerField()),
                ('user_to', models.PositiveSmallIntegerField()),
                ('amount', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='FoodRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('venue', models.PositiveSmallIntegerField()),
                ('poster', models.PositiveSmallIntegerField()),
                ('item', models.CharField(max_length=40)),
                ('cost', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('phone', models.CharField(max_length=20)),
            ],
        ),
    ]
