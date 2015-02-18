# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empresas', '0004_auto_20150214_0049'),
    ]

    operations = [
        migrations.AddField(
            model_name='empresa',
            name='latitud',
            field=models.IntegerField(default=-99.1696),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='empresa',
            name='longitud',
            field=models.IntegerField(default=19.5225),
            preserve_default=True,
        ),
    ]
