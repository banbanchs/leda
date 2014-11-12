# coding=utf-8

from rest_framework import viewsets
from .models import AirCondition, AirAverage
from .serializers import AirAverageSerializer, AirConditionSerializer


class AirConditionViewSets(viewsets.ReadOnlyModelViewSet):
    queryset = AirCondition.objects.all().order_by('-time')[:24]    # 24 hours
    serializer_class = AirConditionSerializer