# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sucursales', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sucursal',
            name='latitud',
            field=models.DecimalField(default=19.5225, max_digits=12, decimal_places=7),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sucursal',
            name='longitud',
            field=models.DecimalField(default=-99.1696, max_digits=12, decimal_places=7),
            preserve_default=True,
        ),
    ]
