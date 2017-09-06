#coding=utf-8

from HTMLParser import HTMLParser
class MLStripper(HTMLParser):
    """
    过滤html方法
    """
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    """
    过滤html方法实现
    """
    if html is None:
        return ""
    s = MLStripper()
    s.feed(html)
    return s.get_data()