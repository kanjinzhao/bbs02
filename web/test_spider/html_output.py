#coding=utf-8
# @Time    : 17-9-8 上午11:17
# @Author  : LIUMINGBO
# @Email   : 540032146@qq.com
import urllib2

import MySQLdb
import time

from jieba import analyse
from jieba.analyse import tfidf

from web import mvhtml


class HtmlOutputer(object):

    def __init__(self):
        self.datas = []

    def collect_data(self,data):
        if data is None:
            return
        self.datas.append(data)


    def output_html(self):
        #输出html文件
        fout = open('out6.html','w')

        fout.write("<html>")
        fout.write("<meta http-equiv=\"Content-Type\" content=\"text/html;charset=utf-8\">")
        fout.write("<body>")
        fout.write("<table>")

        for data in self.datas:

            fout.write("<tr>")
            fout.write("<td>%s</td>" % data['url'])
            #fout.write("<td>%s</td>" % data['head_img'])
            #fout.write("<td>%s</td>" % data['title'].encode('utf-8'))
            #fout.write("<td>%s</td>" % data['summary'].encode('utf-8'))

            fout.write("</tr>")

        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")


        fout.close()

        #存入数据库
        db = MySQLdb.connect("101.200.208.135", "python", "admin!@#", "bbs",charset="utf8")
        cursor = db.cursor()
        insert = ("INSERT INTO web_article(title,categroy_id,head_img,content,author_id,publish_date,hideden,weight,keywords,description)" "VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")




        x = 0
        for data in self.datas:
            title = data['title'].encode('utf-8')
            author_id = '2'
            categroy_id = '2'
            #下载图片
            #urllib2.urlretrieve(data['head_img'],'/home/lmb/bbs02/static/uploads\\d.jpg'%x)
            url = data['head_img']
            f = open('/home/lmb/bbs02/static/uploads/'+str(x)+'.jpg','w')
            req = urllib2.urlopen(url)
            buf = req.read()
            f.write(buf)

            tim = int(time.time())

            head_img = 'static/uploads/'+str(x) + str(tim) +'.jpg'
            x=x+1

            #关键词
            #textrank = analyse.textrank
            keywords = tfidf(data['summary'])
            #循环组合前3个关键词
            arr = []
            n=0
            for s in keywords:
                selecttag = "SELECT num from web_tags WHERE tagname ='%s'" % (s)
                print selecttag
                cursor.execute(selecttag)
                results = cursor.fetchall()
                # 循环保存到tags表
                try:
                    if len(results) ==0:
                        # tag不存在直接插入keyword
                        inserttag = ("INSERT INTO web_tags(tagname,num)" "VALUES(%s,%s)")
                        print inserttag
                        datatag = (s, 1)
                        cursor.execute(inserttag, datatag)
                        db.commit()
                    else:
                        for row in results:
                            num = int(row[0])
                            num = num + 1
                            updatetag = "UPDATE web_tags SET num = '%s'  WHERE tagname ="%(num) + "\'"+ s +"\'"
                            cursor.execute(updatetag)
                            db.commit()
                except:
                    return

                n=n+1
                arr.append(s)
                if n==3:
                    break
            strs = ','.join(arr)
            keywords =strs

            content = data['summary'].encode('utf-8')

            description = mvhtml.strip_tags(content[0:200])

            ISOTIMEFORMAT ='%Y-%m-%d %X'
            publish_date = time.strftime(ISOTIMEFORMAT, time.localtime(time.time()))
            hideden = '0'
            weight = '1000'
            data = (title, categroy_id, head_img, content, author_id,publish_date,hideden,weight,keywords,description)
            try:
                cursor.execute(insert, data)
            except:
                return
        db.commit()

        db.close()


