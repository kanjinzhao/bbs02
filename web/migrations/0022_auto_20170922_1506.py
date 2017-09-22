# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0021_tags_update_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='pv',
            field=models.IntegerField(default=10, verbose_name='\u6d4f\u89c8\u91cf'),
        ),
        migrations.AlterField(
            model_name='tags',
            name='num',
            field=models.CharField(max_length=100, verbose_name='\u9891\u7387'),
        ),
        migrations.AlterField(
            model_name='tags',
            name='tagname',
            field=models.CharField(max_length=20, verbose_name='\u5173\u952e\u5b57'),
        ),
    ]
