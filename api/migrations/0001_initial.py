# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AirAverage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pm2_5', models.FloatField()),
                ('aqi', models.IntegerField()),
                ('city', models.CharField(default=b'Guangzhou', max_length=255)),
                ('definition', models.IntegerField()),
                ('from_time', models.DateTimeField()),
                ('to_time', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AirCondition',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pm2_5', models.FloatField()),
                ('aqi', models.IntegerField()),
                ('time', models.DateTimeField()),
                ('city', models.CharField(default=b'Guangzhou', max_length=255)),
                ('definition', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
