# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empresas', '0005_auto_20150218_0522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresa',
            name='latitud',
            field=models.DecimalField(default=-99.1696, max_digits=8, decimal_places=4),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='empresa',
            name='longitud',
            field=models.DecimalField(default=19.5225, max_digits=8, decimal_places=4),
            preserve_default=True,
        ),
    ]
