# coding=utf-8
__author__ = "Dmitry Zhiltsov"
__copyright__ = "Copyright 2015, Dmitry Zhiltsov"

from django.contrib.auth.admin import admin

from guest_book.models import GuestBook, GuestBookMessages
from web.admin import admin_site


class _BaseGuestBookAdmin(admin.ModelAdmin):
    def _check_sp(self):
        return self.admin_site.name == 'service_panel'

    def has_module_permission(self, request):
        if self._check_sp():
            return True
        return super(_BaseGuestBookAdmin, self).has_module_permission(request)

    def has_add_permission(self, request):
        if self._check_sp():
            return True
        return super(_BaseGuestBookAdmin, self).has_add_permission(request)

    def has_change_permission(self, request, obj=None):
        if self._check_sp():
            return True
        return super(_BaseGuestBookAdmin, self).has_change_permission(request, obj=obj)

    def has_delete_permission(self, request, obj=None):
        if self._check_sp():
            return True
        return super(_BaseGuestBookAdmin, self).has_delete_permission(request, obj=obj)


class GuestBookAdmin(_BaseGuestBookAdmin):
    list_display = ['name', 'is_moderated']
    list_filter = ('is_moderated', )

    fieldsets = ((None, {
        'classes': ('wide',),
        'fields': ('name', 'slug', 'is_moderated')}),)

    def save_model(self, request, obj, form, change):
        if form.is_valid():
            if not request.user.is_staff:
                obj.owner = request.user
            obj.save()

    def get_queryset(self, request):
        qs = super(GuestBookAdmin, self).get_queryset(request)
        if not request.user.is_staff:
            qs = qs.filter(owner=request.user)
        return qs


class GuestBookMessagesAdmin(_BaseGuestBookAdmin):
    list_filter = ('is_visible', 'guest_book',)
    list_display = ['author', 'guest_book', 'is_visible']
    readonly_fields = ['guest_book', 'author', 'time_of_moderate', 'message']

    def get_queryset(self, request):
        qs = super(GuestBookMessagesAdmin, self).get_queryset(request)
        if not request.user.is_staff:
            qs = qs.filter(guest_book__owner=request.user)
        return qs


admin.site.register(GuestBook, GuestBookAdmin)
admin.site.register(GuestBookMessages, GuestBookMessagesAdmin)
admin_site.register(GuestBook, GuestBookAdmin)
admin_site.register(GuestBookMessages, GuestBookMessagesAdmin)
