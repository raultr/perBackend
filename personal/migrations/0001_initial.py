# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('catalogos_detalle', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('matricula', models.IntegerField(unique=True)),
                ('paterno', models.CharField(max_length=20)),
                ('materno', models.CharField(max_length=20)),
                ('nombre', models.CharField(max_length=20)),
                ('rfc', models.CharField(max_length=13)),
                ('curp', models.CharField(max_length=8)),
                ('cuip', models.CharField(max_length=30)),
                ('fec_nacimiento', models.DateField(auto_now_add=True)),
                ('id_seguridad_social', models.CharField(max_length=20)),
                ('portacion', models.BooleanField(default=False)),
                ('cdu_escolaridad', models.ForeignKey(related_name='pesonal_cdu_escolaridad', default=b'', to='catalogos_detalle.CatalogoDetalle')),
                ('cdu_estado_nac', models.ForeignKey(related_name='pesonal_cdu_estado_nac', default=b'', validators=[django.core.validators.RegexValidator(regex=b'(?=^.{7,7}$)(^014)([0-9]{4})', message=b'El catalogo debe empezar con 14 y su longitud de 7', code=b'nomatch')], to='catalogos_detalle.CatalogoDetalle')),
                ('cdu_municipio_nac', models.ForeignKey(related_name='pesonal_cdu_municipio_nac', default=b'', to='catalogos_detalle.CatalogoDetalle')),
                ('cdu_religion', models.ForeignKey(related_name='pesonal_cdu_religion', default=b'', to='catalogos_detalle.CatalogoDetalle')),
                ('cdu_seguridad_social', models.ForeignKey(related_name='pesonal_cdu_seguridad_social', default=b'', to='catalogos_detalle.CatalogoDetalle')),
            ],
            options={
                'verbose_name': 'personal',
                'verbose_name_plural': 'personal',
            },
            bases=(models.Model,),
        ),
    ]
