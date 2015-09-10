# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20150910_1230'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tariffplan',
            options={'verbose_name': 'Tariff Plan', 'verbose_name_plural': 'Tariff Plans'},
        ),
    ]
