#coding=utf-8
import jieba
from jieba import analyse

tfidf = analyse.extract_tags

textrank = analyse.textrank

text ="无轨电车落地济南！8条详细线路出炉 2021年建成"

seg_list = jieba.cut(text, cut_all=True)
print "Full Mode:", "/ ".join(seg_list)  # 全模式

seg_list = jieba.cut(text, cut_all=False)
print "Default Mode:", "/ ".join(seg_list)  # 默认模式

seg_list = jieba.cut(text)
print "/ ".join(seg_list)


keywords = tfidf(text)

print keywords
trkeywords = textrank(text)

print "tfidf分词："

for keyword in keywords:
    print keyword + "/",

print ""

print "textrank分词："

for keyword in trkeywords:
    print keyword + "/",


str ="agc,雅思报名"
print str.split("，")