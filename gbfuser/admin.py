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

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
        ('GBF info', {'fields': ('tariff_plan',)})
    )

admin.site.register(GBFUser, GBFUserAdmin)
