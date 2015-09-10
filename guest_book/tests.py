# coding=utf-8
__author__ = "Dmitry Zhiltsov"
__copyright__ = "Copyright 2015, Dmitry Zhiltsov"

from django.test import TestCase

from core.models import TariffPlan
from gbfuser.errors import LimitExceeded
from gbfuser.models import GBFUser
from guest_book.defs import GuestBookMessageData, GuestBookCreateData
from guest_book.models import GuestBook


class GuestBookTestCase(TestCase):
    fixtures = ['core.json', 'gbfuser.json']

    def setUp(self):
        self.tariff_start = TariffPlan.objects.get(name='Start')
        self.tariff_unlim = TariffPlan.objects.get(name='Unlimeted')
        self.gb_owner = GBFUser.objects.get(username='dzhiltsov', tariff_plan=self.tariff_unlim)
        self.gb_message_author = GBFUser.objects.get(username='vano', tariff_plan=self.tariff_start)

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

    def testLimitCreateBook(self):
        with self.assertRaises(LimitExceeded) as exc:
            self.gb_message_author.create_gb(GuestBookCreateData(name='Test1', slug='test1'))
            self.gb_message_author.create_gb(GuestBookCreateData(name='Test2', slug='test2', is_moderated=False))
            self.gb_message_author.create_gb(GuestBookCreateData(name='Test3', slug='test3'))
            self.gb_message_author.create_gb(GuestBookCreateData(name='Test4', slug='test4'))
        self.assertEqual(exc.exception.limit, self.gb_message_author.tariff_plan.gb_limit)

    def testCreateGuestBookMessage(self):
        gb1, gb2 = self._create_gbs()
        msg_gb1 = gb1.create_message(GuestBookMessageData(message="Hello, World", author_id=self.gb_message_author.id))
        msg_gb2 = gb2.create_message(GuestBookMessageData(message="Hello, World1", author_id=self.gb_message_author.id))
        self.assertFalse(msg_gb1.is_visible)
        self.assertTrue(msg_gb2.is_visible)

    def testApproveGuestBookMessage(self):
        gb1, gb2 = self._create_gbs()
        msg_gb1 = gb1.create_message(GuestBookMessageData(message="Hello, World", author_id=self.gb_message_author.id))
        self.assertFalse(msg_gb1.is_visible)
        self.assertTrue(msg_gb1.approve_message())
        self.assertTrue(msg_gb1.is_visible)
        self.assertFalse(msg_gb1.approve_message())
