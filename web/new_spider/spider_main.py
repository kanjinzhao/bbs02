#coding=utf-8
# @Time    : 17-9-25 下午5:47
# @Author  : LIUMINGBO
# @Email   : 540032146@qq.com

from web.new_spider import url_manage,html_download,html_parser,html_output

class SpiderMain(object):
    def __init__(self):

        #采集url
        self.urls = url_manage.UrlManager()


    def craw(self, root_url):
            #记数
            count = 1
            #添加入口url
            self.urls.add_new_url(root_url)
            #启动爬虫循环
            #当url管理器中有url时循环
            while self.urls.has_new_url():
                try:
                    #获取一个url
                    new_url = self.urls.get_new_url()
                    print 'craw %d:%s' % (count,new_url)
                    #启动下载器，下载页面，结果存储在html_cont
                    html_cont = self.downloader.download(new_url)

                    #下载页面后，利用parser解析器解析数据
                    new_urls,new_data = self.parser.parse(new_url,html_cont)
                    #将解析出的url添加到url管理器
                    self.urls.add_new_urls(new_urls)
                    #收集数据
                    self.outputer.collect_data(new_data)
                    #爬取1000个页面
                    if count==50:
                        break

                    count=count+1
                except:
                    print 'craw failed'

            #output 输出收集的数据
            self.outputer.output_html()


if __name__=="__main__":
    #root_url="http://www.baike.com/wiki/%E8%96%9B%E4%B9%8B%E8%B0%A6"
    #root_url="https://baike.baidu.com/item/%E8%96%9B%E4%B9%8B%E8%B0%A6/144417"
    root_url = "http://www.zmnedu.com/bk/zx/"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
