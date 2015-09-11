# coding=utf-8
__author__ = "Dmitry Zhiltsov"
__copyright__ = "Copyright 2015, Dmitry Zhiltsov"

from django import forms

from guest_book.models import GuestBook


class CreateGBForm(forms.ModelForm):
    class Meta:
        model = GuestBook
        fields = ['name', 'slug', 'is_moderated']
