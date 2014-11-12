# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='airaverage',
            old_name='definition',
            new_name='level',
        ),
        migrations.RenameField(
            model_name='aircondition',
            old_name='definition',
            new_name='level',
        ),
    ]
