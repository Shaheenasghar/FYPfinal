# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-07-22 13:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_auto_20170722_1212'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='partner',
            new_name='customer',
        ),
    ]
