#coding=utf-8
# @Time    : 17-11-23 下午3:02
# @Author  : LIUMINGBO
# @Email   : 540032146@qq.com
import urllib2

import time
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver import ActionChains

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import bs4 as bs
from bs4 import BeautifulSoup




def main():
    # 设置 user agent
    dcap = dict(DesiredCapabilities.PHANTOMJS)
    dcap['phantomjs.page.settings.userAgent'] = (
        'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0'
    )

    #driver = webdriver.PhantomJS(desired_capabilities=dcap)

    driver = webdriver.Firefox()



    # 通过主页面获取相关session
    #driver.get('http://www.lagou.com')
    #driver.get('https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=')
    #driver.get('http://bbs.qyer.com')
    driver.get('http://bbs.qyer.com/forum-2-1.html')
    time.sleep(3)
    # 滚动条下拉1000px
    js = "document.documentElement.scrollTop=20000"
    driver.execute_script(js)
    #driver.implicitly_wait(30)

    time.sleep(3)

    #driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    #time.sleep(5)

    # 解析页面
    soup = bs.BeautifulSoup(driver.page_source, 'html.parser')
    print soup
    # 使用 css 选择器
    #items = soup.select('.con_list_item')
    items = soup.select('.imgwp')

    # 输出招聘信息
    x=1
    for item in items:
        print('*' * 40)
        #print(item['data-company'])
        #print(item['data-positionname'])
        #print(item['data-salary'])
        #print(item)
        imgcode = item.find('img')
        # 下载图片
        url = imgcode['src']
        #tim = int(time.time())
        x = x + 1
        print x
        try:
            f = open('/home/lmb/bbs02/static/uploads/'+str(x)+'.jpg','w')
            req = urllib2.urlopen(url)
            buf = req.read()
            f.write(buf)
            #print (imgcode)
            print (item)
        except:
            print ('异常')


if __name__ == '__main__':
    main()