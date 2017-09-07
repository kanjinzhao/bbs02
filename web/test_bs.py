#coding=utf-8
from bs4 import BeautifulSoup
import re


html_doc = """
<html><head><title>The Dormouse's story</title></head>

<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc,'html.parser',from_encoding='utf-8')

print '获取所有链接'
links = soup.find_all('a')
print links
for link in links:
    print link.name,link['href'],link.get_text(),link['class'],link['id']

print '获取其中一个链接'
linkone = soup.find('a',href="http://example.com/lacie")
linkid = soup.find('a',id="link1")
print linkone
print '按id获取链接'
print linkid

print '按正则表达式'
linkzz = soup.find('a',href=re.compile(r"cie"))
print linkzz

print '按class获取'
textp = soup.find('p',class_='title')
print textp,textp
print textp.name
print textp.get_text()