# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uniformes_detalle', '0002_auto_20161006_0413'),
    ]

    operations = [
        migrations.RenameField(
            model_name='uniformedetalle',
            old_name='id_uniforme',
            new_name='uniforme',
        ),
    ]
