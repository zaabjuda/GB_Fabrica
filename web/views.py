# coding=utf-8
__author__ = "Dmitry Zhiltsov"
__copyright__ = "Copyright 2015, Dmitry Zhiltsov"

from django.contrib.auth import logout, decorators
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, RedirectView, CreateView, DetailView, UpdateView, ListView

from guest_book.defs import GuestBookMessageData
from guest_book.models import GuestBook, GuestBookMessages

from .forms import CreateMessageForm


class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return decorators.login_required(view)


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


class AddGB(LoginRequiredMixin, CreateView):
    model = GuestBook
    fields = ['name', 'slug', 'is_moderated']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(AddGB, self).form_valid(form)


class _BaseGBDetail(LoginRequiredMixin, DetailView):
    def get_object(self, queryset=None):
        owner = self.kwargs.get('owner')
        if not queryset:
            queryset = GuestBook.objects
        queryset = queryset.filter(owner__username=owner)

        return super(_BaseGBDetail, self).get_object(queryset=queryset)


class _BaseGBUpdate(LoginRequiredMixin, UpdateView):
    def get_object(self, queryset=None):
        owner = self.kwargs.get('owner')
        if not queryset:
            queryset = GuestBook.objects
        queryset = queryset.filter(owner__username=owner)

        return super(_BaseGBUpdate, self).get_object(queryset=queryset)


class ViewGB(LoginRequiredMixin, _BaseGBDetail):
    model = GuestBook


class AddMessage(LoginRequiredMixin, _BaseGBUpdate):
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


class SettingsGB(LoginRequiredMixin, _BaseGBUpdate):
    model = GuestBook
    fields = ['name', 'slug', 'is_moderated']

    def get_object(self, queryset=None):
        owner = self.kwargs.get('owner')
        if not queryset:
            queryset = GuestBook.objects
        queryset = queryset.filter(owner__username=owner, owner=self.request.user)
        return super(SettingsGB, self).get_object(queryset=queryset)


class UserGBs(LoginRequiredMixin, ListView):
    model = GuestBook

    def get_queryset(self):
        qs = super(UserGBs, self).get_queryset()
        qs = qs.filter(owner=self.request.user)
        return qs
