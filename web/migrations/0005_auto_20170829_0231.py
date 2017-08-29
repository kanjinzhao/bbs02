# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_auto_20170817_0257'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='parent_commment',
            new_name='parent_comment',
        ),
        migrations.AlterField(
            model_name='article',
            name='content',
            field=ckeditor.fields.RichTextField(null=True, verbose_name=b'\xe6\x96\x87\xe7\xab\xa0\xe5\x86\x85\xe5\xae\xb9', blank=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='head_img',
            field=models.ImageField(upload_to=b'static/uploads', verbose_name='\u7f29\u7565\u56fe'),
        ),
        migrations.AlterField(
            model_name='article',
            name='publish_date',
            field=models.DateTimeField(auto_now=True, verbose_name='\u53d1\u5e03\u65f6\u95f4'),
        ),
    ]
