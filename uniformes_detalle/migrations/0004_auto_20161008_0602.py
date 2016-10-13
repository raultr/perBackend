# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('uniformes_detalle', '0003_auto_20161008_0547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uniformedetalle',
            name='uniforme',
            field=models.ForeignKey(related_name='detalle_uniforme', on_delete=django.db.models.deletion.PROTECT, to='uniformes.Uniforme', null=True),
            preserve_default=True,
        ),
    ]
