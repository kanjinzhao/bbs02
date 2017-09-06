#coding=utf-8

import urllib2

request = urllib2.Request("http://www.kejiwang.cn")

try:
    response = urllib2.urlopen(request,timeout=3)
except urllib2.URLError,e:
    print e.reason
print response.read()