#coding=utf-8
# @Time    : 17-9-26 下午4:22
# @Author  : LIUMINGBO
# @Email   : 540032146@qq.com
class NewsUrlManger(object):
    #构造函数初始化
    def __init__(self):
        self.new_urls = set()
        self.old_urls =set()

    def add_new_url(self, url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)


    def add_new_urls(self,urls):
        if urls is None or len(urls)==0:
            return
        for url in urls:
            self.add_new_url(url)


    def has_new_url(self):
        return len(self.new_urls) != 0

    def get_new_url(self):
        #pop()方法是从列表冲获取一个url，并移除此url
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url

