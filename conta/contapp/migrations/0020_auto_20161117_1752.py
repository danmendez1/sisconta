# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-11-17 23:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contapp', '0019_partida_concepto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movimiento',
            name='debe',
            field=models.FloatField(blank=True, default=0.0),
        ),
        migrations.AlterField(
            model_name='movimiento',
            name='haber',
            field=models.FloatField(blank=True, default=0.0),
        ),
    ]