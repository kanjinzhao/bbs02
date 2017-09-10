#coding=utf-8
# @Time    : 17-9-8 上午11:17
# @Author  : LIUMINGBO
# @Email   : 540032146@qq.com
import MySQLdb
import time


class HtmlOutputer(object):

    def __init__(self):
        self.datas = []

    def collect_data(self,data):
        if data is None:
            return
        self.datas.append(data)


    def output_html(self):

        fout = open('out6.html','w')

        fout.write("<html>")
        fout.write("<meta http-equiv=\"Content-Type\" content=\"text/html;charset=utf-8\">")
        fout.write("<body>")
        fout.write("<table>")

        for data in self.datas:

            fout.write("<tr>")
            fout.write("<td>%s</td>" % data['url'])
            fout.write("<td>%s</td>" % data['title'].encode('utf-8'))
            fout.write("<td>%s</td>" % data['summary'].encode('utf-8'))
            fout.write("</tr>")

        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")


        fout.close()

        #存入数据库
        db = MySQLdb.connect("101.200.208.135", "python", "admin!@#", "bbs",charset="utf8")
        cursor = db.cursor()
        insert = ("INSERT INTO web_article(title,categroy_id,head_img,content,author_id,publish_date,hideden,weight)" "VALUES(%s,%s,%s,%s,%s,%s,%s,%s)")
        for data in self.datas:
            title = data['title'].encode('utf-8')
            author_id = '2'
            categroy_id = '2'
            head_img = 'uploads/1.jpg'
            content = data['summary'].encode('utf-8')
            ISOTIMEFORMAT ='%Y-%m-%d %X'
            publish_date =time.strftime(ISOTIMEFORMAT, time.localtime(time.time()))
            hideden = '0'
            weight = '1000'
            data = (title, categroy_id, head_img, content, author_id,publish_date,hideden,weight)
            cursor.execute(insert, data)
        db.commit()


