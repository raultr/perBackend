# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0003_auto_20141211_0402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personal',
            name='curp',
            field=models.CharField(max_length=8),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='personal',
            name='nombre',
            field=models.CharField(max_length=20, validators=[django.core.validators.RegexValidator(regex=b'(?=^.{7,7}$)(^014)([0-9]{4})', message=b'El catalogo debe empezar con 14 y su longitud de 7', code=b'nomatch')]),
            preserve_default=True,
        ),
    ]
