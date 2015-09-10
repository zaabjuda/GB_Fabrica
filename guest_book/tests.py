# coding=utf-8
__author__ = "Dmitry Zhiltsov"
__copyright__ = "Copyright 2015, Dmitry Zhiltsov"

from django.test import TestCase
from gbfuser.models import GBFUser
from guest_book.models import GuestBook


class GuestBookTestCase(TestCase):
    fixtures = ['core.json', 'gbfuser.json']

    def setUp(self):
        self.gb_owner = GBFUser.objects.get(username='dzhiltsov')
        self.gb_message_author = GBFUser.objects.get(username='vano')

    def testCreateGuestBook(self):
        gb1 = GuestBook.objects.create(name='test_gbook1', slug='test_gbook1', owner=self.gb_owner)
        gb2 = GuestBook.objects.create(name='test_gbook2', slug='test_gbook2', owner=self.gb_owner, is_moderated=False)
        self.assertTrue(gb1.is_moderated)
        self.assertFalse(gb2.is_moderated)
