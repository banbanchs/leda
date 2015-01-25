# coding=utf-8

from django.db import models


class AirCondition(models.Model):
    """Record air condition hourly"""
    pm2_5 = models.FloatField()
    aqi = models.IntegerField()
    time = models.DateTimeField(db_index=True)
    city = models.CharField(max_length=255, default='Guangzhou', db_index=True)
    level = models.IntegerField()

    class Meta:
        ordering = ['-time']


class AirAverage(models.Model):
    """Record air condition daily (12h)"""
    pm2_5 = models.FloatField()
    aqi = models.IntegerField()
    city = models.CharField(max_length=255, default='Guangzhou', db_index=True)
    level = models.IntegerField()
    from_time = models.DateTimeField(db_index=True)
    to_time = models.DateTimeField()

    class Meta:
        ordering = ['-from_time']
