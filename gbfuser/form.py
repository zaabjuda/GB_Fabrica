# coding=utf-8
__author__ = "Dmitry Zhiltsov"
__copyright__ = "Copyright 2015, Dmitry Zhiltsov"

from django.contrib.auth.forms import UserCreationForm, UserChangeForm, ReadOnlyPasswordHashField
from django.forms import CharField, PasswordInput, ValidationError

from gbfuser.models import GBFUser


class GBFUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = GBFUser
        fields = ('email', 'username')


class GBFUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = GBFUser
        fields = ('username', 'email', 'password', 'is_active', 'is_staff', 'is_superuser', 'user_permissions', 'tariff_plan')

    def clean_password(self):
        return self.initial['password']
