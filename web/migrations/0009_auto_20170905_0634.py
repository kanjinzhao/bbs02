# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0008_auto_20170905_0632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='keywords',
            field=models.CharField(default=b'', max_length=255, verbose_name='\u6587\u7ae0\u5173\u952e\u5b57', blank=True),
        ),
    ]
