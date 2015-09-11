# coding=utf-8
__author__ = "Dmitry Zhiltsov"
__copyright__ = "Copyright 2015, Dmitry Zhiltsov"

from django.contrib import admin


class MyAdminSite(admin.AdminSite):
    site_header = 'GBF-ServicePanel'
    site_title = site_header

    def has_permission(self, request):
        return request.user.is_active


admin_site = MyAdminSite()
