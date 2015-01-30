# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0002_auto_20141211_0341'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='personal',
            options={'verbose_name': 'personal', 'verbose_name_plural': 'personal'},
        ),
    ]
