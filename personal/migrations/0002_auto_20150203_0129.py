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
            name='curp',
            field=models.CharField(max_length=18),
            preserve_default=True,
        ),
    ]
