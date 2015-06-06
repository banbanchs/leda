# coding=utf-8

from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = format_suffix_patterns([
    url(r'pm25/(?P<city>\w+)/latest$', views.AirConditionViewSets.as_view({'get': 'list'}), name='pm25-list'),
    url(r'pm25-avg/(?P<city>\w+)/latest$', views.AirAverageViewSets.as_view({'get': 'list'}), name='pm25-avg-list'),
])
