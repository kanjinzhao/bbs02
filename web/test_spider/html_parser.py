#coding=utf-8
# @Time    : 17-9-8 上午11:17
# @Author  : LIUMINGBO
# @Email   : 540032146@qq.com

import urlparse

import re
from bs4 import BeautifulSoup

from web.test_spider import html_download


class HtmlParser(object):

    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        #获取搜狗所有的链接    格式 http://www.baike.com/wiki/***
        #links = soup.find_all('a',href=re.compile(r"http://www.baike.com/wiki/(.*)"))
        #获取搜狗特定区域的链接
        contentcode = soup.find('div',class_="main-content")
        #if '美国'.decode("utf-8") in contentcode.get_text():
            #/item/**/123
            #links = contentcode.find_all('a', href=re.compile(r"/item/(.*)"))
        links = contentcode.find_all('a',href=re.compile(r"/item/(.*)"))
        for link in links:
                new_url = link['href']

                new_full_url = urlparse.urljoin(page_url,new_url)
                new_urls.add(new_full_url)
        return new_urls


    def _get_new_data(self, page_url, soup):
        res_data = {}

        res_data['url'] = page_url
        #<h1 style="line-height: 51px;">薛之谦<em class="f24">[中国内地歌手]</em></h1>
        #< dd   class ="lemmaWgt-lemmaTitle-title" >< h1 > 薛之谦 < / h1 >
        title_node = soup.find('dd',class_="lemmaWgt-lemmaTitle-title").find('h1')
        res_data['title'] = title_node.get_text()
        #< div class ="summary" name="anchor" id="anchor" > < p > ***< / p > < / div >
        #<div class="lemma-summary" label-module="lemmaSummary">
        summary_node = soup.find('div',class_="lemma-summary")
        res_data['summary'] = summary_node.get_text()
        #获取图片链接
        img_node = soup.find('div',class_="summary-pic").find('img')
        res_data['head_img'] = img_node['src']

        print  img_node

        return res_data



    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont,'html.parser',from_encoding='utf=8')
        new_urls = self._get_new_urls(page_url,soup)
        new_data = self._get_new_data(page_url,soup)
        return new_urls,new_data
