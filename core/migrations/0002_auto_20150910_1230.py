# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tariffplan',
            name='name',
            field=models.CharField(max_length=24, unique=True, verbose_name='Tariff name'),
        ),
    ]
