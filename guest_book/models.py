# coding=utf-8
__author__ = "Dmitry Zhiltsov"
__copyright__ = "Copyright 2015, Dmitry Zhiltsov"

from datetime import datetime as dt

from django.db import models
from django.conf import settings

from gbfuser.models import GBFUser


class GuestBookMessageManager(models.Manager):
    def create_message(self, message_data):
        is_visible = not self.guest_book.is_moderated
        gb_message = self.create(is_visible=is_visible, **message_data)
        return gb_message


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
    objects = GuestBookMessageManager()

    guest_book = models.ForeignKey(GuestBook)
    message = models.TextField('Message')  # TODO Align limit
    author = models.ForeignKey(GBFUser)
    time_of_creation = models.DateTimeField(auto_now_add=True)
    is_visible = models.BooleanField()
    time_of_moderate = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name = 'Guest Book Message'
        verbose_name_plural = 'Guest Books Messages'

    def approve_message(self):
        """
        This method used when owner GB execute approve action on message

        :return: self
        """
        if self.is_visible:
            return self
        self.is_visible = True
        self.time_of_moderate = dt.now()
        self.save()
        return self

    def __str__(self):
        return "Author: {} Guest Book: {} Guest Book Owner: {}".format(self.guest_book.name, self.guest_book.owner,
                                                                       self.author)
