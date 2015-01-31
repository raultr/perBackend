# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catalogo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('icono', models.ImageField(upload_to=b'catalogos', blank=True)),
                ('url_icono', models.CharField(default=b'', max_length=255, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
