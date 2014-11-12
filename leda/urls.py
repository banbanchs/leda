# coding=utf-8

from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'pm25', views.AirConditionViewSets)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'api/', include('rest_framework.urls', namespace='rest_framework'))
]