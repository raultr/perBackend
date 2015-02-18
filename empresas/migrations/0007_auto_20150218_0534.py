# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empresas', '0006_auto_20150218_0533'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empresa',
            name='latitud',
        ),
        migrations.RemoveField(
            model_name='empresa',
            name='longitud',
        ),
    ]
