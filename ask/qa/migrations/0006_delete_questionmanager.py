# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-20 08:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0005_questionmanager'),
    ]

    operations = [
        migrations.DeleteModel(
            name='QuestionManager',
        ),
    ]
