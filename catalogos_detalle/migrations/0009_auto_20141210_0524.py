# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogos_detalle', '0008_auto_20141124_0543'),
    ]

    operations = [
        migrations.RenameField(
            model_name='catalogodetalle',
            old_name='udc_catalogo',
            new_name='cdu_catalogo',
        ),
        migrations.RenameField(
            model_name='catalogodetalle',
            old_name='udc_default',
            new_name='cdu_default',
        ),
    ]
