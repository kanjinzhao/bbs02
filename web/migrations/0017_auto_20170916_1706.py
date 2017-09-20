# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0016_tags'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tags',
            old_name='update_time',
            new_name='updat_time',
        ),
    ]
