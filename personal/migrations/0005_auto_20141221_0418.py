# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0004_auto_20141212_0606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personal',
            name='cdu_estado_nac',
            field=models.ForeignKey(related_name='pesonal_cdu_estado_nac', default=b'', to_field=b'cdu_catalogo', validators=[django.core.validators.RegexValidator(regex=b'(?=^.{7,7}$)(^014)([0-9]{4})', message=b'El catalogo debe empezar con 14 y su longitud de 7', code=b'nomatch')], to='catalogos_detalle.CatalogoDetalle'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='personal',
            name='nombre',
            field=models.CharField(max_length=20),
            preserve_default=True,
        ),
    ]
