#coding=utf-8

# Create your tests here.
import MySQLdb

def test():
    db = MySQLdb.connect("101.200.208.135", "python", "admin!@#", "bbs")
    print('连接上了!')
    cursor = db.cursor()
    insert = ("INSERT INTO web_article(title,categroy_id,head_img,content,author_id)" "VALUES(%s,%s,%s,%s,%s)")
    title ='ceshibiaoti4'
    author_id ='2'
    categroy_id = '2'
    head_img = 'uploads/1.jgp'
    content = 'neirong'
    data = (title,categroy_id,head_img,content,author_id)
    cursor.execute(insert,data)
    db.commit()

    #b=models.Article(title=title,categroy_id=categroy_id,head_img=head_img,content=content)
    #b.save()


