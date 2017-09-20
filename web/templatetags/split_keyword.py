#coding=utf-8
# @Time    : 17-9-20 下午5:12
# @Author  : LIUMINGBO
# @Email   : 540032146@qq.com
from django import template

register = template.Library()

#自动拆分关键词

def truncate_chars(value):
  if value.__len__() > 0:
    return value.split(',')
  else:
    return ''
register.filter('truncate_chars',truncate_chars)