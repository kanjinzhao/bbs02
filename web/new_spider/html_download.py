#coding=utf-8
# @Time    : 17-9-26 下午4:22
# @Author  : LIUMINGBO
# @Email   : 540032146@qq.com
import urllib2


class HtmlDownLodader(object):
    def download(self, url):
        if url is None:
            return None
        response = urllib2.urlopen(url)

        if response.getcode() != 200:
            return None
        return response.read()
