# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-27 10:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EventModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tick', models.TimeField(unique=True)),
                ('title', models.TextField(max_length=30)),
                ('comment', models.TextField(max_length=1000)),
            ],
        ),
    ]
