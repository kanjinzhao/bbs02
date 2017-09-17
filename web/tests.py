#coding=utf-8

# Create your tests here.
import time

import MySQLdb

def test():
    db = MySQLdb.connect("101.200.208.135", "python", "admin!@#", "bbs",charset='utf8')
    print('连接上了!')
    cursor = db.cursor()
    insert = ("INSERT INTO web_article(title,categroy_id,head_img,content,author_id)" "VALUES(%s,%s,%s,%s,%s)")
    title ='ceshibiaoti4'
    author_id ='2'
    categroy_id = '2'
    head_img = 'uploads/1.jgp'
    content = 'neirong'
    #data = (title,categroy_id,head_img,content,author_id)
    #cursor.execute(insert,data)


    #select
    s='山东'
    selecttag = "SELECT num from web_tags WHERE tagname ='%s'"%(s)
    #selecttag = "SELECT * from web_tags"

    print selecttag
    try:
        cursor.execute(selecttag)
        results = cursor.fetchall()
        print results
        if len(results) == 0:
            print "执行插入"
        else:
            print "执行更新"
    except:
        return
    for s in results:
        print int(s[0])+1

    #update
    num = 3
    s= '山东'
    updatetag = "UPDATE web_tags SET num = '%s'  WHERE tagname ="%(num) +"\'"+s+"\'"
    print updatetag
    cursor.execute(updatetag)


    db.commit()
    db.close()

    #b=models.Article(title=title,categroy_id=categroy_id,head_img=head_img,content=content)
    #b.save()


#test()
#print time.time()
#print int(time.time())
