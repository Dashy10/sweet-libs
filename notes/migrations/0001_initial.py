# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-08 19:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=120)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
