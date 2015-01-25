# coding=utf-8

import views
from rest_framework import routers


api_router = routers.DefaultRouter()
api_router.register(r'pm25/(?P<city>\w+)/lastest', views.AirConditionViewSets, base_name='pm25')
api_router.register(r'pm25-avg/(?P<city>\w+)/lastest', views.AirAverageViewSets, base_name='pm25-avg')
