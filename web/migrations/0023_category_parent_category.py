# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0022_auto_20170922_1506'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='parent_category',
            field=models.ForeignKey(related_name='p_category', verbose_name=b'\xe7\x88\xb6\xe6\xa0\x8f\xe7\x9b\xae', blank=True, to='web.Category', null=True),
        ),
    ]
