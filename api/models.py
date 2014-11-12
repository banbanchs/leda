# coding=utf-8

from django.db import models


class AirCondition(models.Model):
    """Record air condition hourly"""
    pm2_5 = models.FloatField()
    aqi = models.IntegerField()
    time = models.DateTimeField()
    city = models.CharField(max_length=255, default='Guangzhou')
    level = models.IntegerField()


class AirAverage(models.Model):
    """Record air condition daily (12h)"""
    pm2_5 = models.FloatField()
    aqi = models.IntegerField()
    city = models.CharField(max_length=255, default='Guangzhou')
    level = models.IntegerField()
    from_time = models.DateTimeField()
    to_time = models.DateTimeField()
