# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guest_book', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guestbookmessages',
            name='time_of_moderate',
            field=models.DateTimeField(null=True),
        ),
    ]
