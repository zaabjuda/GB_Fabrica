# coding=utf-8
__author__ = "Dmitry Zhiltsov"
__copyright__ = "Copyright 2015, Dmitry Zhiltsov"

from django.contrib.auth import logout
from django.views.generic import TemplateView, RedirectView, CreateView, DetailView

from guest_book.models import GuestBook


class IndexView(TemplateView):
    template_name = 'index.html'


class LogoutView(RedirectView):
    """
    Provides users the ability to logout
    """
    url = '/'

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)


class AddGB(CreateView):
    model = GuestBook
    fields = ['name', 'slug', 'is_moderated']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(AddGB, self).form_valid(form)


class ViewGB(DetailView):
    model = GuestBook
