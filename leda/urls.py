# coding=utf-8

from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'pm25', views.AirConditionViewSets)
router.register(r'pm25_avg', views.AirAverageViewSets)

urlpatterns = [
    url(r'^$', include('home.urls', namespace='home')),
    url(r'^api/', include(router.urls)),
    # url(r'api/', include('rest_framework.urls', namespace='rest_framework')),
]
