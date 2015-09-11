# coding=utf-8
__author__ = "Dmitry Zhiltsov"
__copyright__ = "Copyright 2015, Dmitry Zhiltsov"

from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, RedirectView, CreateView, DetailView, UpdateView, ListView

from guest_book.defs import GuestBookMessageData
from guest_book.models import GuestBook, GuestBookMessages

from .forms import CreateMessageForm


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


class _BaseGBDetail(DetailView):
    def get_object(self, queryset=None):
        owner = self.kwargs.get('owner')
        if not queryset:
            queryset = GuestBook.objects
        queryset = queryset.filter(owner__username=owner)

        return super(_BaseGBDetail, self).get_object(queryset=queryset)


class _BaseGBUpdate(UpdateView):
    def get_object(self, queryset=None):
        owner = self.kwargs.get('owner')
        if not queryset:
            queryset = GuestBook.objects
        queryset = queryset.filter(owner__username=owner)

        return super(_BaseGBUpdate, self).get_object(queryset=queryset)


class ViewGB(_BaseGBDetail):
    model = GuestBook


class AddMessage(_BaseGBUpdate):
    template_name = 'create_message.html'
    template_name_suffix = ''
    model = GuestBook
    form_class = CreateMessageForm

    def form_valid(self, form):
        message = form.data.get('message')
        msg_data = GuestBookMessageData(message=message, author_id=self.request.user.id)
        gb = self.get_object()
        gb.create_message(msg_data)
        return HttpResponseRedirect(self.get_success_url())


class SettingsGB(_BaseGBUpdate):
    model = GuestBook
    fields = ['is_moderated']


class UserGBs(ListView):
    pass
