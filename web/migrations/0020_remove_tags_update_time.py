# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0019_tags_update_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tags',
            name='update_time',
        ),
    ]
