#coding=utf-8
# @Time    : 17-9-8 上午11:17
# @Author  : LIUMINGBO
# @Email   : 540032146@qq.com
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