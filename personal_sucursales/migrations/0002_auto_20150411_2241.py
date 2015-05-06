# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personal_sucursales', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalsucursal',
            name='motivo',
            field=models.CharField(max_length=100, blank=True),
            preserve_default=True,
        ),
    ]
