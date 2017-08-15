# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='hideden',
            field=models.BooleanField(default=False, verbose_name='\u662f\u5426\u9690\u85cf'),
        ),
    ]
