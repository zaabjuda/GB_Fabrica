# coding=utf-8
__author__ = "Dmitry Zhiltsov"
__copyright__ = "Copyright 2015, Dmitry Zhiltsov"

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from gbfuser.form import GBFUserChangeForm, GBFUserCreationForm
from gbfuser.models import GBFUser


class GBFUserAdmin(UserAdmin):
    form = GBFUserChangeForm
    add_form = GBFUserCreationForm


admin.site.register(GBFUser, GBFUserAdmin)
