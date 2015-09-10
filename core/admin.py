# coding=utf-8
__author__ = "Dmitry Zhiltsov"
__copyright__ = "Copyright 2015, Dmitry Zhiltsov"

from django.contrib import admin

from core.models import TariffPlan


class TariffPlanAdmin(admin.ModelAdmin):
    pass


admin.site.register(TariffPlan, TariffPlanAdmin)
