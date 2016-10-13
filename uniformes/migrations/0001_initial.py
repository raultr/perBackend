# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0008_auto_20160820_0136'),
    ]

    operations = [
        migrations.CreateModel(
            name='Uniforme',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField(default=b'1900-01-01')),
                ('anio', models.IntegerField(default=0)),
                ('periodo', models.IntegerField(default=0)),
                ('observaciones', models.CharField(max_length=200, blank=True)),
                ('id_personal', models.ForeignKey(related_name='personaluniforme_id_personal', on_delete=django.db.models.deletion.PROTECT, to='personal.Personal', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
