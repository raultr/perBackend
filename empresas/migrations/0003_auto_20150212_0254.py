# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empresas', '0002_auto_20150212_0252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresa',
            name='telefono2',
            field=models.CharField(max_length=10),
            preserve_default=True,
        ),
    ]
