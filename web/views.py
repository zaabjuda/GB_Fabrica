# coding=utf-8
__author__ = "Dmitry Zhiltsov"
__copyright__ = "Copyright 2015, Dmitry Zhiltsov"


from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'
