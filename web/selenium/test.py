#coding=utf-8
# @Time    : 17-11-7 下午2:47
# @Author  : LIUMINGBO
# @Email   : 540032146@qq.com


from selenium import webdriver
from selenium.webdriver.common.keys import Keys


browser = webdriver.Firefox()

browser.get('http://www.baidu.com')

elem = browser.find_element_by_name("wd")
word = '科技网'.decode('utf-8')
elem.send_keys(word)
elem.send_keys(Keys.RETURN)

print browser.page_source