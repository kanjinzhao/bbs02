#coding=utf-8
# @Time    : 17-11-7 下午2:47
# @Author  : LIUMINGBO
# @Email   : 540032146@qq.com

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


browser = webdriver.Firefox()

browser.get('http://bbs.qyer.com/forum-2-1.html')

#elem = browser.find_element_by_name("wd")
#word = '科技网'.decode('utf-8')
#elem.send_keys(word)
#elem.send_keys(Keys.RETURN)
#time.sleep(5)
#browser.find_element_by_class_name("n").click()


num = 1
while (num < 9):
    print '第'+ str(num) +'页'
    browser.find_element_by_xpath("//a[contains(text(),'下一页')]").click()
    time.sleep(5)

    num = num + 1



#elem.send_keys("",Keys.ARROW_DOWN)

print browser.page_source