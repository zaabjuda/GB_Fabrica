# coding=utf-8
__author__ = "Dmitry Zhiltsov"
__copyright__ = "Copyright 2015, Dmitry Zhiltsov"

from django.db import models
from django.conf import settings

from gbfuser.models import GBFUser


class GuestBook(models.Model):
    name = models.CharField('Guest Book Name', max_length=250)
    slug = models.SlugField('Guest Book Slug', max_length=50)
    owner = models.ForeignKey(GBFUser)
    is_moderated = models.BooleanField('Is moderated?', default=getattr(settings, 'GB_PREMODERATE_DEFAULT', True))

    class Meta:
        verbose_name = 'Guest Book'
        verbose_name_plural = 'Guest Books'
        unique_together = (('name', 'owner',), ('slug', 'owner'),)

    def __str__(self):
        return "{} Owned by {} ".format(self.name, self.owner.get_full_name())


class GuestBookMessages(models.Model):
    guest_book = models.ForeignKey(GuestBook)
    message = models.TextField('Message') #TODO Align limit
    author = models.ForeignKey(GBFUser)
    time_of_creation = models.DateTimeField(auto_now_add=True)
    is_visible = models.BooleanField()
    time_of_moderate = models.DateTimeField(blank=True)

    class Meta:
        verbose_name = 'Guest Book Message'
        verbose_name_plural = 'Guest Books Messages'
