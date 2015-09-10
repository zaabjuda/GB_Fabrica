# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TariffPlan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(unique=True, max_length='24', verbose_name='Tariff name')),
                ('price', models.PositiveSmallIntegerField(verbose_name='Price in $')),
                ('gb_limit', models.PositiveSmallIntegerField(verbose_name='Limit for Guest Book')),
            ],
        ),
    ]
