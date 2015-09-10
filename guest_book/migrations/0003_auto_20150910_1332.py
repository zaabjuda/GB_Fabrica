# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guest_book', '0002_auto_20150910_1328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guestbookmessages',
            name='time_of_moderate',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
