#coding=utf-8
import urllib2

from bs4 import BeautifulSoup
import re

url = "https://baike.baidu.com/item/%E8%96%9B%E4%B9%8B%E8%B0%A6/144417"

print "Frist Method"
response1 = urllib2.urlopen(url)
html_doc = response1.read()
#print html_doc
ftext = open("bake.html","w")
ftext.write(html_doc)

soup = BeautifulSoup(html_doc,'html.parser',from_encoding='utf-8')
#/item/%E4%BD%A0%E8%BF%87%E5%BE%97%E5%A5%BD%E5%90%97/16742992
print '获取所有链接'
links = soup.find_all('a', href=re.compile(r"/item/(.*)"))
content = soup.find('div',class_="main-content").get_text()
#links = soup.find_all('a')
s= '薛之谦'.decode('utf-8')
if '薛之谦'.decode("utf-8") in content:
    print content
#print links
count = 1
for link in links:
    new_urls =set()
    #print link.name,link['href']
    new_urls.add(link)
    if count ==100:
        break

    count = count+1
    #print new_urls
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