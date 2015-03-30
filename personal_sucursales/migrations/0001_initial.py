# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0007_auto_20150226_0351'),
        ('sucursales', '0002_auto_20150328_0439'),
        ('catalogos_detalle', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalSucursal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sueldo', models.DecimalField(default=0.0, max_digits=12, decimal_places=7)),
                ('fecha_inicial', models.DateField(default=b'1900-01-01')),
                ('fecha_final', models.DateField(default=b'1900-01-01')),
                ('motivo', models.CharField(max_length=100)),
                ('cdu_motivo', models.ForeignKey(related_name=' personalsucursal_cdu_motivo', default=b'', to='catalogos_detalle.CatalogoDetalle')),
                ('cdu_puesto', models.ForeignKey(related_name=' personalsucursal_cdu_puesto', default=b'', to='catalogos_detalle.CatalogoDetalle')),
                ('cdu_rango', models.ForeignKey(related_name=' personalsucursal_cdu_rango', default=b'', to='catalogos_detalle.CatalogoDetalle')),
                ('cdu_turno', models.ForeignKey(related_name=' personalsucursal_cdu_turno', default=b'', to='catalogos_detalle.CatalogoDetalle')),
                ('id_personal', models.ForeignKey(related_name='personalsucursal_id_personal', to='personal.Personal')),
                ('id_sucursal', models.ForeignKey(related_name='personalsucursal_id_sucursal', to='sucursales.Sucursal')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
