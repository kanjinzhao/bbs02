#coding=utf-8
# @Time    : 17-9-22 下午3:25
# @Author  : LIUMINGBO
# @Email   : 540032146@qq.com
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
PROFILE = os.environ.get('DJANGO_SELFBLOG_PROFILE', 'develop')  # 我是把settings.py拆成了：develop.py,product.py
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bbs02.settings.%s" % PROFILE)
app = Celery('selfblog', broker="redis://127.0.0.1:6666/2")
app.config_from_object('django.conf:settings', namespace='CELERY')
# Load task modules from all registered Django app configs.
app.autodiscover_tasks()