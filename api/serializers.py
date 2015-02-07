# coding=utf-8

from rest_framework import serializers
from .models import AirCondition, AirAverage


class AirConditionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AirCondition
        fields = ('pm2_5', 'aqi', 'city', 'level', 'time')


class AirAverageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AirAverage
        fields = ('pm2_5', 'aqi', 'city', 'level', 'from_time', 'to_time')
