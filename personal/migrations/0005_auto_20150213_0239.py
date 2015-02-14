# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0004_auto_20150212_0430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personal',
            name='fec_alta',
            field=models.DateField(default=b'1900-01-01'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='personal',
            name='fec_nacimiento',
            field=models.DateField(default=b'1900-01-01'),
            preserve_default=True,
        ),
    ]
