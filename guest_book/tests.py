# coding=utf-8
__author__ = "Dmitry Zhiltsov"
__copyright__ = "Copyright 2015, Dmitry Zhiltsov"

from django.test import TestCase

from gbfuser.models import GBFUser
from guest_book.defs import GuestBookMessageData
from guest_book.models import GuestBook, GuestBookMessages


class GuestBookTestCase(TestCase):
    fixtures = ['core.json', 'gbfuser.json']

    def setUp(self):
        self.gb_owner = GBFUser.objects.get(username='dzhiltsov')
        self.gb_message_author = GBFUser.objects.get(username='vano')

    def _create_gbs(self):
        gb1, created1 = GuestBook.objects.get_or_create(name='test_gbook1', slug='test_gbook1', owner=self.gb_owner)
        gb2, created2 = GuestBook.objects.get_or_create(name='test_gbook2', slug='test_gbook2', owner=self.gb_owner,
                                                        is_moderated=False)
        gb1.save()
        gb2.save()
        return gb1, gb2

    def testCreateGuestBook(self):
        gb1, gb2 = self._create_gbs()
        self.assertTrue(gb1.is_moderated)
        self.assertFalse(gb2.is_moderated)

    def testCreateGuestBookMessage(self):
        gb1, gb2 = self._create_gbs()
        msg_gb1 = gb1.create_message(GuestBookMessageData(message="Hello, World", author_id=self.gb_message_author.id))
        msg_gb2 = gb2.create_message(GuestBookMessageData(message="Hello, World", author_id=self.gb_message_author.id))
        self.assertFalse(msg_gb1.is_visible)
        self.assertTrue(msg_gb2.is_visible)
