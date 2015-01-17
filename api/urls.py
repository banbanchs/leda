# coding=utf-8

import views
from rest_framework import routers


api_router = routers.DefaultRouter()
api_router.register(r'pm25', views.AirConditionViewSets, base_name='pm25')
api_router.register(r'pm25-avg', views.AirAverageViewSets, base_name='pm25-avg')
