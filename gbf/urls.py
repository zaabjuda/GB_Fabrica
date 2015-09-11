"""gbf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

from web.views import AddGB, IndexView, LogoutView, ViewGB

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^add/$', AddGB.as_view(), name='add_gb'),
    url(r'^gb/(?P<owner>\w{1,30})/(?P<slug>\w{1,50})/$', ViewGB.as_view(), name='gb_view'),
]
