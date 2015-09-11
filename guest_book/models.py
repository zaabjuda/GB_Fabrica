# coding=utf-8
__author__ = "Dmitry Zhiltsov"
__copyright__ = "Copyright 2015, Dmitry Zhiltsov"

from datetime import datetime as dt

from django.core.urlresolvers import reverse
from django.conf import settings
from django.db import models

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

    def create_message(self, message_data):
        """
        :param message_data:
        :type message_data: GuestBookMessageData
        :return:
        :rtype: GuestBookMessages
        """
        is_visible = not self.is_moderated
        gb_message = GuestBookMessages.objects.create(is_visible=is_visible, guest_book=self, **message_data.to_dict())
        return gb_message

    def get_visible_messages(self):
        qs = self.guestbookmessages_set.all()
        if self.is_moderated:
            qs = qs.filter(is_visible=True)
        return qs

    def get_moderate_messages(self):
        return self.guestbookmessages_set.filter(is_visible=False)

    def get_absolute_url(self):
        return reverse('gb_view', kwargs={'slug': self.slug, 'owner': self.owner.username})

    def __str__(self):
        return "{} Owned by {} ".format(self.name, self.owner.get_full_name())


class GuestBookMessages(models.Model):
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

        :return: True if is_visible field changed, False if is_visible field already is True
        """
        if self.is_visible:
            return False
        self.is_visible = True
        self.time_of_moderate = dt.now()
        self.save()
        return True

    def __str__(self):
        return "Author: {} Guest Book: {} Guest Book Owner: {}".format(self.author, self.guest_book.name,
                                                                       self.guest_book.owner)
