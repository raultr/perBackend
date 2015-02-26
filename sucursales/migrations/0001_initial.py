# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogos_detalle', '0001_initial'),
        ('empresas', '0010_auto_20150218_0601'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cve_sucursal', models.IntegerField(unique=True)),
                ('nombre', models.CharField(max_length=150)),
                ('calle', models.CharField(max_length=100)),
                ('numero', models.CharField(max_length=10)),
                ('colonia', models.CharField(max_length=100)),
                ('cp', models.CharField(max_length=10)),
                ('ciudad', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=10)),
                ('fecha_alta', models.DateField(default=b'1900-01-01')),
                ('fecha_baja', models.DateField(default=b'1900-01-01')),
                ('latitud', models.DecimalField(default=-99.1696, max_digits=12, decimal_places=7)),
                ('longitud', models.DecimalField(default=19.5225, max_digits=12, decimal_places=7)),
                ('cdu_estado', models.ForeignKey(related_name='sucursal_cdu_estado', default=b'', to='catalogos_detalle.CatalogoDetalle')),
                ('cdu_estatus', models.ForeignKey(related_name='sucursal_cdu_estatus', default=b'', to='catalogos_detalle.CatalogoDetalle')),
                ('cdu_municipio', models.ForeignKey(related_name='sucursal_cdu_municipio', default=b'', to='catalogos_detalle.CatalogoDetalle')),
                ('cve_empresa', models.ForeignKey(related_name='empresa_sucursal', to='empresas.Empresa')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
