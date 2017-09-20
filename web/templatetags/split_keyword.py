#coding=utf-8
# @Time    : 17-9-20 下午5:12
# @Author  : LIUMINGBO
# @Email   : 540032146@qq.com
from django import template

register = template.Library()

# 若字符串长度大于30，则省略之后的内容，否则原样输出该字符串。参数value就是过滤器前的值

def truncate_chars(value):
  if value.__len__() > 0:
    return value.split(',')
  else:
    return ''
register.filter('truncate_chars',truncate_chars)


#    keywords = article.keywords
#    if keywords is not None:
#        article.keywords = keywords.split(',')