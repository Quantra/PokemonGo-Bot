# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0003_auto_20160818_1938'),
    ]

    operations = [
        migrations.CreateModel(
            name='CatchLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_date', models.DateTimeField(null=True, verbose_name=b'Creation Date')),
                ('mod_date', models.DateTimeField(null=True, verbose_name=b'Last Modified')),
                ('username', models.CharField(max_length=255)),
                ('encounter_id', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
