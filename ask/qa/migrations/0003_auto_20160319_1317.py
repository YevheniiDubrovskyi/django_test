# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-19 13:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0002_auto_20160313_1813'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionManager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='answer',
            name='added_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='added_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]