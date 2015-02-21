# coding=utf-8

from rest_framework import routers

from . import views


api_router = routers.DefaultRouter()
api_router.register(r'pm25/(?P<city>\w+)/latest', views.AirConditionViewSets, base_name='pm25')
api_router.register(r'pm25-avg/(?P<city>\w+)/latest', views.AirAverageViewSets, base_name='pm25-avg')
