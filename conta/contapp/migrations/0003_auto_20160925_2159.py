# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-26 03:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contapp', '0002_auto_20160925_2118'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rubcuenta',
            old_name='codTipo',
            new_name='codRubro',
        ),
        migrations.RenameField(
            model_name='rubcuenta',
            old_name='nomTipo',
            new_name='nomRubro',
        ),
    ]
