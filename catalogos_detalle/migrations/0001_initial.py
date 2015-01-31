# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from decimal import Decimal


class Migration(migrations.Migration):

    dependencies = [
        ('catalogos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CatalogoDetalle',
            fields=[
                ('cdu_catalogo', models.CharField(primary_key=True, default=b'0000000', serialize=False, editable=False, max_length=7, unique=True)),
                ('num_dcatalogo', models.IntegerField(default=0, help_text=b'clave consecutiva del detalle del catalogo')),
                ('descripcion1', models.CharField(max_length=255)),
                ('descripcion2', models.CharField(max_length=255, blank=True)),
                ('monto1', models.DecimalField(default=Decimal('0.00'), max_digits=18, decimal_places=2)),
                ('monto2', models.DecimalField(default=Decimal('0.00'), max_digits=18, decimal_places=2)),
                ('cdu_default', models.CharField(max_length=7, blank=True)),
                ('catalogos', models.ForeignKey(related_name='catalogos_detalle', to='catalogos.Catalogo')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
