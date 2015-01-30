# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogos_detalle', '0009_auto_20141210_0524'),
    ]

    operations = [
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('matricula', models.SmallIntegerField()),
                ('paterno', models.CharField(max_length=20)),
                ('materno', models.CharField(max_length=20)),
                ('nombre', models.CharField(max_length=20)),
                ('rfc', models.CharField(max_length=13)),
                ('curp', models.CharField(max_length=18)),
                ('cuip', models.CharField(max_length=30)),
                ('fec_nacimiento', models.DateField(auto_now_add=True)),
                ('cdu_estado_nac', models.CharField(max_length=7)),
                ('cdu_municipio_nac', models.CharField(max_length=7)),
                ('cdu_religion', models.CharField(max_length=7)),
                ('cdu_seguridad_social', models.CharField(max_length=7)),
                ('id_seguridad_social', models.CharField(max_length=20)),
                ('portacion', models.BooleanField(default=False)),
                ('cdu_escolaridad', models.ForeignKey(related_name='pesonal_cdu_escolaridad', default=b'', to_field=b'cdu_catalogo', to='catalogos_detalle.CatalogoDetalle')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
