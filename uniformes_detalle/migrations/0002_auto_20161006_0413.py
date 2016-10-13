# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('uniformes', '0001_initial'),
        ('catalogos_detalle', '0001_initial'),
        ('uniformes_detalle', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UniformeDetalle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cdu_concepto_uniforme', models.ForeignKey(related_name='uniformedetalle_cdu_uniforme', on_delete=django.db.models.deletion.PROTECT, default=b'', to='catalogos_detalle.CatalogoDetalle')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='uniforme',
            name='cdu_concepto_uniforme',
        ),
        migrations.RemoveField(
            model_name='uniforme',
            name='id_uniforme',
        ),
        migrations.DeleteModel(
            name='Uniforme',
        ),
        migrations.AddField(
            model_name='uniformedetalle',
            name='id_uniforme',
            field=models.ForeignKey(related_name='detalle_id_uniforme', on_delete=django.db.models.deletion.PROTECT, to='uniformes.Uniforme', null=True),
            preserve_default=True,
        ),
    ]
