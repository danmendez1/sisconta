# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-27 03:44
from __future__ import unicode_literals

import contapp.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contapp', '0004_movimiento_idcuenta'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movimiento',
            old_name='idmovimiento',
            new_name='idMovimiento',
        ),
        migrations.AlterField(
            model_name='movimiento',
            name='idCuenta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contapp.cuenta'),
        ),
    ]
