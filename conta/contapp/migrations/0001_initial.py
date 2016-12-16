# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-25 19:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cuenta',
            fields=[
                ('idCuenta', models.IntegerField(primary_key=True, serialize=False)),
                ('codCuenta', models.CharField(max_length=15)),
                ('nomCuenta', models.CharField(max_length=50)),
                ('grado', models.IntegerField()),
                ('idCuentaPadre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contapp.cuenta')),
            ],
        ),
        migrations.CreateModel(
            name='empresa',
            fields=[
                ('codEmpresa', models.IntegerField(primary_key=True, serialize=False)),
                ('nomEmpresa', models.CharField(max_length=100)),
                ('nit', models.CharField(max_length=50)),
                ('nrc', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='fecha',
            fields=[
                ('idFecha', models.IntegerField(primary_key=True, serialize=False)),
                ('dia', models.IntegerField()),
                ('mes', models.IntegerField()),
                ('anio', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='movimiento',
            fields=[
                ('idmovimiento', models.IntegerField(primary_key=True, serialize=False)),
                ('debe', models.FloatField()),
                ('haber', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='partida',
            fields=[
                ('idPartida', models.IntegerField(primary_key=True, serialize=False)),
                ('numPartida', models.IntegerField()),
                ('codEmpresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contapp.empresa')),
                ('idFecha', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contapp.fecha')),
            ],
        ),
        migrations.CreateModel(
            name='rubCuenta',
            fields=[
                ('idRubro', models.IntegerField(primary_key=True, serialize=False)),
                ('codTipo', models.CharField(max_length=15)),
                ('nomTipo', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='tipCuenta',
            fields=[
                ('idTipo', models.IntegerField(primary_key=True, serialize=False)),
                ('codTipo', models.CharField(max_length=15)),
                ('nomTipo', models.CharField(max_length=50)),
                ('codEmpresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contapp.empresa')),
            ],
        ),
        migrations.AddField(
            model_name='rubcuenta',
            name='idTipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contapp.tipCuenta'),
        ),
        migrations.AddField(
            model_name='movimiento',
            name='idPartida',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contapp.partida'),
        ),
        migrations.AddField(
            model_name='cuenta',
            name='idRubro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contapp.rubCuenta'),
        ),
    ]