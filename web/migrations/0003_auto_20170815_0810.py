# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_auto_20170815_0806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='parent_commment',
            field=models.ForeignKey(related_name='p_comment', blank=True, to='web.Comment', null=True),
        ),
    ]
