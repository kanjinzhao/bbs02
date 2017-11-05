#coding=utf-8
# @Time    : 17-9-26 下午4:23
# @Author  : LIUMINGBO
# @Email   : 540032146@qq.com
import urlparse

import re
from bs4 import BeautifulSoup


class HtmlParser(object):

    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        #获取搜狗所有的链接    格式 http://www.baike.com/wiki/***
        #links = soup.find_all('a',href=re.compile(r"http://www.baike.com/wiki/(.*)"))
        #获取搜狗特定区域的链接
        contentcode = soup.find('div',class_="lt_list")
        #if '唐嫣'.decode("utf-8") in contentcode.get_text():
            #/item/**/123
            #links = soup.find_all('a',href=re.compile(r"http://www.baike.com/wiki/(.*)"))
        #links = contentcode.find_all('a',href=re.compile(r"/item/(.*)"))
        links = contentcode.find_all('a',href=re.compile(r"/(\d+).html"))

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
        #title_node = soup.find('div',class_="ds_title ffyh pos_r").find('h1')
        title_node = soup.find('h1',class_="fwb")
        #标题
        res_data['title'] = title_node.get_text()
        #文章内容
        content_node = soup.find('div',class_="ds_cr")
        #过滤文章图片
        content_node.img.decompose()
        #过滤文章图片
        content_node.table.decompose()
        new_content = str(content_node)
        #print key

        #key = '<div class="ds_cr"><p>根据美国马萨诸塞</p><br><div id="pageurl">adad'
        p1 = r'(?<=<div class="ds_cr">)([\s\S]*?)(?=<div id="pageurl">)'  # 这是我们写的正则表达式规则，你现在可以不理解啥意思
        #p1 = r'(?<=<div class="fs14">)(.*?)(?=</div>)'
        pattern1 = re.compile(p1)  # 我们在编译这段正则表达式
        matcher1 = re.search(pattern1, new_content)  # 在源文本中搜索符合正则表达式的部分
        content_node = matcher1.group(0)  # 打印出来
        #print  content_node


        #content_node.select('.fs14').decompose()




        #content_node.div(class_="fs14").decompose()
        #div_fs14 = content_node.div
        #div_fs14.decompose()
        #content_node.img.decompose()


        res_data['body'] = content_node

        res_data['head_img']="static/uploads/401505789957.jpg"


        #res_data['description'] = content_node[0:200]


        #关键词

        #< div class ="summary" name="anchor" id="anchor" > < p > ***< / p > < / div >
        #<div class="lemma-summary" label-module="lemmaSummary">
        #summary_node = soup.find('div',class_="lemma-summary")
        #res_data['summary'] = summary_node.get_text()
        #获取图片链接
        #img_node = soup.find('div',class_="summary-pic").find('img')
        #res_data['head_img'] = img_node['src']
        #print res_data['title']

        return res_data



    def parseroot(self, page_url, html_cont):

        if page_url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont,'html.parser',from_encoding='utf=8')
        new_urls = self._get_new_urls(page_url,soup)
        #print new_urls
        #new_data = self._get_new_data(page_url,soup)

        return new_urls


    def parsenews(self, page_url, html_cont):

        if page_url is None:
            return

        soup = BeautifulSoup(html_cont,'html.parser',from_encoding='utf=8')
        new_data = self._get_new_data(page_url,soup)
        return new_data
