# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
        ('gbfuser', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gbfuser',
            name='tariff_plan',
            field=models.ForeignKey(to='core.TariffPlan', null=True),
        ),
    ]
