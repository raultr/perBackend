# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empresas', '0003_auto_20150212_0254'),
    ]

    operations = [
        migrations.RenameField(
            model_name='empresa',
            old_name='id_empresa',
            new_name='cve_empresa',
        ),
        migrations.AlterField(
            model_name='empresa',
            name='fecha_alta',
            field=models.DateField(default=b'1900-01-01'),
            preserve_default=True,
        ),
    ]
