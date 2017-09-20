# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0020_remove_tags_update_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='tags',
            name='update_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 16, 9, 31, 24, 587929, tzinfo=utc), verbose_name='\u66f4\u65b0\u65f6\u95f4', auto_now=True),
            preserve_default=False,
        ),
    ]
