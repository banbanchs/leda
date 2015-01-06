# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20141112_1403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airaverage',
            name='city',
            field=models.CharField(default=b'Guangzhou', max_length=255, db_index=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='airaverage',
            name='from_time',
            field=models.DateTimeField(db_index=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='aircondition',
            name='city',
            field=models.CharField(default=b'Guangzhou', max_length=255, db_index=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='aircondition',
            name='time',
            field=models.DateTimeField(db_index=True),
            preserve_default=True,
        ),
    ]
