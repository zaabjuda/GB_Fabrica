# coding=utf-8
__author__ = "Dmitry Zhiltsov"
__copyright__ = "Copyright 2015, Dmitry Zhiltsov"

from django.contrib.auth.admin import admin

from guest_book.models import GuestBook, GuestBookMessages


class GuestBookAdmin(admin.ModelAdmin):
    pass


class GuestBookMessagesAdmin(admin.ModelAdmin):
    pass


admin.site.register(GuestBook, GuestBookAdmin)
admin.site.register(GuestBookMessages, GuestBookMessagesAdmin)
