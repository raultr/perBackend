# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0005_auto_20150213_0239'),
    ]

    operations = [
        migrations.AddField(
            model_name='personal',
            name='imagen',
            field=models.ImageField(default=b'', upload_to=b'personal', blank=True),
            preserve_default=True,
        ),
    ]
