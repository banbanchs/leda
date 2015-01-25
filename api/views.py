# coding=utf-8

import logging
from rest_framework import viewsets
from .models import AirCondition, AirAverage
from .serializers import AirAverageSerializer, AirConditionSerializer


class AirConditionViewSets(viewsets.ReadOnlyModelViewSet):
    serializer_class = AirConditionSerializer
    lookup_url_kwarg = 'city'

    def get_queryset(self):
        city_name = self.kwargs.get(self.lookup_url_kwarg)
        queryset = AirCondition.objects.filter(city=city_name)
        return queryset[:12]


class AirAverageViewSets(viewsets.ReadOnlyModelViewSet):
    serializer_class = AirAverageSerializer
    lookup_url_kwarg = 'city'

    def get_queryset(self):
        city_name = self.kwargs.get(self.lookup_url_kwarg)
        queryset = AirAverage.objects.filter(city=city_name)
        return queryset[:10]
