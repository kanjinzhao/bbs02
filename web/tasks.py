#coding=utf-8
# @Time    : 17-9-22 下午3:43
# @Author  : LIUMINGBO
# @Email   : 540032146@qq.com
from __future__ import unicode_literals
from django.db.models import F
from .models import Article
from bbs02.celery import app
@app.task
def increase_pv(post_id):
    return Article.objects.filter(id=post_id).update(pv=F('pv')+1)
#@app.task
#def increase_uv(post_id):
#    return Article.objects.filter(id=post_id).update(uv=F('uv')+1)