# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0006_auto_20141222_0311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personal',
            name='matricula',
            field=models.IntegerField(unique=True),
            preserve_default=True,
        ),
    ]
