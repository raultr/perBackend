# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogos_detalle', '0001_initial'),
        ('personal', '0002_auto_20150203_0129'),
    ]

    operations = [
        migrations.AddField(
            model_name='personal',
            name='cdu_estado_civil',
            field=models.ForeignKey(related_name='pesonal_cdu_estado_civil', default=b'0010000', to='catalogos_detalle.CatalogoDetalle'),
            preserve_default=True,
        ),
    ]
