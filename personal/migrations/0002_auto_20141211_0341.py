# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personal',
            name='cdu_estado_nac',
            field=models.ForeignKey(related_name='pesonal_cdu_estado_nac', default=b'', to_field=b'cdu_catalogo', to='catalogos_detalle.CatalogoDetalle'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='personal',
            name='cdu_municipio_nac',
            field=models.ForeignKey(related_name='pesonal_cdu_municipio_nac', default=b'', to_field=b'cdu_catalogo', to='catalogos_detalle.CatalogoDetalle'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='personal',
            name='cdu_religion',
            field=models.ForeignKey(related_name='pesonal_cdu_religion', default=b'', to_field=b'cdu_catalogo', to='catalogos_detalle.CatalogoDetalle'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='personal',
            name='cdu_seguridad_social',
            field=models.ForeignKey(related_name='pesonal_cdu_seguridad_social', default=b'', to_field=b'cdu_catalogo', to='catalogos_detalle.CatalogoDetalle'),
            preserve_default=True,
        ),
    ]
