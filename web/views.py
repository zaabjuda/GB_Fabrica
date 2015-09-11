# coding=utf-8
__author__ = "Dmitry Zhiltsov"
__copyright__ = "Copyright 2015, Dmitry Zhiltsov"

from django.contrib.auth import logout
from django.views.generic import TemplateView, RedirectView, CreateView, DetailView, UpdateView, ListView

from guest_book.models import GuestBook


class IndexView(TemplateView):
    template_name = 'index.html'


class LogoutView(RedirectView):
    """
    Provides users the ability to logout
    """
    permanent = True
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

    def get_object(self, queryset=None):
        owner = self.kwargs.get('owner')
        if not queryset:
            queryset = GuestBook.objects
        queryset = queryset.filter(owner__username=owner)

        return super(ViewGB, self).get_object(queryset=queryset)


class AddMessage(CreateView):
    pass


class SettingsGB(UpdateView):
    pass


class UserGBs(ListView):
    pass
