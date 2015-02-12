# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('catalogos_detalle', '0001_initial'),
        ('personal', '0003_personal_cdu_estado_civil'),
    ]

    operations = [
        migrations.AddField(
            model_name='personal',
            name='calle_dom',
            field=models.CharField(default=b'', max_length=100),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='personal',
            name='cdu_estado_dom',
            field=models.ForeignKey(related_name='pesonal_cdu_estado', default=b'0140000', to='catalogos_detalle.CatalogoDetalle'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='personal',
            name='cdu_municipio_dom',
            field=models.ForeignKey(related_name='pesonal_cdu_municipio', default=b'0150000', to='catalogos_detalle.CatalogoDetalle'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='personal',
            name='cdu_tipo_alta',
            field=models.ForeignKey(related_name='pesonal_cdu_tipo_alta', default=b'0200000', to='catalogos_detalle.CatalogoDetalle'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='personal',
            name='cdu_tipo_empleado',
            field=models.ForeignKey(related_name='pesonal_tipo_empleado', default=b'0210000', to='catalogos_detalle.CatalogoDetalle'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='personal',
            name='ciudad_dom',
            field=models.CharField(default=b'', max_length=100),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='personal',
            name='colonia_dom',
            field=models.CharField(default=b'', max_length=100),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='personal',
            name='condicionada',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='personal',
            name='condiciones_alta',
            field=models.CharField(default=b'', max_length=150),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='personal',
            name='cp_dom',
            field=models.CharField(default=b'', max_length=10),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='personal',
            name='fec_alta',
            field=models.DateField(default=datetime.datetime(2015, 2, 12, 4, 30, 13, 754045, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='personal',
            name='numero_dom',
            field=models.CharField(default=b'', max_length=10),
            preserve_default=True,
        ),
    ]
