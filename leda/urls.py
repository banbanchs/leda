# coding=utf-8

from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$', include('home.urls', namespace='home')),
    url(r'^api/', include('api.urls', namespace='api')),
]
