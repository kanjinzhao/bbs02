# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0023_category_parent_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='parent_category',
            field=models.ForeignKey(related_name='p_category', default=0, verbose_name=b'\xe7\x88\xb6\xe6\xa0\x8f\xe7\x9b\xae', to='web.Category'),
        ),
    ]
