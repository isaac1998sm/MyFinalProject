# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2020-09-10 09:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addresses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='country',
            field=models.CharField(default='iran', max_length=120),
        ),
    ]