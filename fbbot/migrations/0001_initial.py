# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-07-22 13:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='partner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('App_id', models.CharField(max_length=100)),
                ('Page_id', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=15)),
            ],
        ),
    ]
