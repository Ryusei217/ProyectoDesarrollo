# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-23 22:18
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0001_corregida_app_perfil'),
    ]

    operations = [
        migrations.CreateModel(
            name='Componente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_comercial', models.CharField(max_length=50, unique=True, verbose_name='Nombre Comercial')),
                ('iupac', models.CharField(max_length=50, unique=True, verbose_name='IUPAC')),
                ('unii', models.CharField(max_length=25, unique=True, verbose_name='UNII')),
                ('formula', models.CharField(max_length=50, verbose_name='Formula')),
                ('peso_molecular', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Peso Molecular')),
                ('biodisponibilidad', models.CharField(blank=True, max_length=25, null=True, verbose_name='Biodisponibilidad')),
                ('union_proteica', models.CharField(blank=True, max_length=25, null=True, verbose_name='Union Proteica')),
                ('metabolismo', models.CharField(blank=True, max_length=25, null=True, verbose_name='Metabolismo')),
                ('vida_media', models.CharField(blank=True, max_length=25, null=True, verbose_name='Vida Media')),
                ('excrecion', models.CharField(blank=True, max_length=25, null=True, verbose_name='Excrecion')),
                ('via_admon', models.CharField(max_length=50, verbose_name='Via de Administracion')),
                ('tipo', models.PositiveSmallIntegerField(choices=[(1, 'Activo'), (2, 'Excipiente')], verbose_name='Tipo')),
                ('creado', models.DateTimeField(auto_now_add=True, verbose_name='Creado')),
                ('fecha_firma', models.DateTimeField(auto_now=True, verbose_name='Fecha Firma')),
                ('firma', models.CharField(blank=True, max_length=255, null=True, verbose_name='Firma Electronica')),
                ('responsable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='componentes', to=settings.AUTH_USER_MODEL, verbose_name='Responsable')),
            ],
            options={
                'verbose_name': 'Componente',
                'verbose_name_plural': 'Componentes',
            },
        ),
    ]
