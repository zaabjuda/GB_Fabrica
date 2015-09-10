# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GuestBook',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name='Guest Book Name', max_length=250)),
                ('slug', models.SlugField(verbose_name='Guest Book Slug')),
                ('is_moderated', models.BooleanField(verbose_name='Is moderated?', default=True)),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Guest Book',
                'verbose_name_plural': 'Guest Books',
            },
        ),
        migrations.CreateModel(
            name='GuestBookMessages',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('message', models.TextField(verbose_name='Message')),
                ('time_of_creation', models.DateTimeField(auto_now_add=True)),
                ('is_visible', models.BooleanField()),
                ('time_of_moderate', models.DateTimeField(blank=True)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('guest_book', models.ForeignKey(to='guest_book.GuestBook')),
            ],
            options={
                'verbose_name': 'Guest Book Message',
                'verbose_name_plural': 'Guest Books Messages',
            },
        ),
        migrations.AlterUniqueTogether(
            name='guestbook',
            unique_together=set([('name', 'owner'), ('slug', 'owner')]),
        ),
    ]
