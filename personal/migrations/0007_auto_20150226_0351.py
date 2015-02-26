# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0006_personal_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personal',
            name='condiciones_alta',
            field=models.CharField(default=b'', max_length=150, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='personal',
            name='cuip',
            field=models.CharField(max_length=30, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='personal',
            name='id_seguridad_social',
            field=models.CharField(max_length=20, blank=True),
            preserve_default=True,
        ),
    ]
