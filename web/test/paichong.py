#coding=utf-8
import cookielib
import urllib2
import bs4

url = "https://baike.baidu.com/item/%E8%96%9B%E4%B9%8B%E8%B0%A6/144417"

print "Frist Method"
response1 = urllib2.urlopen(url)
print response1.read()
print response1.getcode()
print len(response1.read())

print "Second Method"
request = urllib2.Request(url)
request.add_header("user-agent","Mozilla/5.0")
response2 = urllib2.urlopen(request)
print response2.getcode()
print len(response2.read())

print "Third Method"
ck = cookielib.CookieJar()
openner = urllib2.build_opener(urllib2.HTTPCookieProcessor(ck))
urllib2.install_opener(openner)
response3 = urllib2.urlopen(url)
print response3.getcode()
print ck
#print response3.read()