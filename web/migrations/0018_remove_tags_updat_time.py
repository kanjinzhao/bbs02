# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0017_auto_20170916_1706'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tags',
            name='updat_time',
        ),
    ]
