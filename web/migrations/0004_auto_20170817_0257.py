# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_auto_20170815_0810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.ForeignKey(verbose_name='\u4f5c\u8005', to='web.UserProfile'),
        ),
        migrations.AlterField(
            model_name='article',
            name='head_img',
            field=models.ImageField(upload_to=b'uploads', verbose_name='\u7f29\u7565\u56fe'),
        ),
        migrations.RemoveField(
            model_name='category',
            name='admin',
        ),
        migrations.AddField(
            model_name='category',
            name='admin',
            field=models.ManyToManyField(to='web.UserProfile', verbose_name='\u7ba1\u7406\u5458'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(unique=True, max_length=64, verbose_name='\u677f\u5757\u540d\u79f0'),
        ),
    ]
