# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogos_detalle', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_empresa', models.IntegerField(unique=True)),
                ('razon_social', models.CharField(max_length=150)),
                ('rfc', models.CharField(max_length=13)),
                ('calle', models.CharField(max_length=100)),
                ('numero', models.CharField(max_length=10)),
                ('colonia', models.CharField(max_length=100)),
                ('cp', models.CharField(max_length=10)),
                ('ciudad', models.CharField(max_length=100)),
                ('telefono1', models.CharField(max_length=10)),
                ('telefono2', models.CharField(max_length=10)),
                ('fecha_alta', models.DateField(auto_now_add=True)),
                ('cdu_estado', models.ForeignKey(related_name='empresa_cdu_estado', default=b'', to='catalogos_detalle.CatalogoDetalle')),
                ('cdu_giro', models.ForeignKey(related_name='empresa_cdu_giro', default=b'', to='catalogos_detalle.CatalogoDetalle')),
                ('cdu_municipio', models.ForeignKey(related_name='empresa_cdu_municipio', default=b'', to='catalogos_detalle.CatalogoDetalle')),
                ('cdu_rubro', models.ForeignKey(related_name='empresa_cdu_rubro', default=b'', to='catalogos_detalle.CatalogoDetalle')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
