# coding=utf-8
__author__ = "Dmitry Zhiltsov"
__copyright__ = "Copyright 2015, Dmitry Zhiltsov"

from django.db import models


class TariffPlan(models.Model):
    name = models.CharField('Tariff name', max_length=24, unique=True)
    price = models.PositiveSmallIntegerField('Price in $')
    gb_limit = models.PositiveSmallIntegerField('Limit for Guest Book')

    class Meta:
        verbose_name = 'Tariff Plan'
        verbose_name_plural = 'Tariff Plans'

    def __str__(self):
        return "{} Limit: {}".format(self.name, self.gb_limit)
