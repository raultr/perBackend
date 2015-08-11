# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sucursales', '0002_auto_20150328_0439'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sucursal',
            name='ciudad',
        ),
    ]
