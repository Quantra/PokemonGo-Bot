# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0002_auto_20160818_1900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login',
            name='create_date',
            field=models.DateTimeField(null=True, verbose_name=b'Creation Date'),
        ),
        migrations.AlterField(
            model_name='login',
            name='mod_date',
            field=models.DateTimeField(null=True, verbose_name=b'Last Modified'),
        ),
    ]
