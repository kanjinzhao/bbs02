#coding=utf-8
# @Time    : 17-9-29 下午5:16
# @Author  : LIUMINGBO
# @Email   : 540032146@qq.com
import re

key = '<html><body><h1>hello world<h1>"sdf"</body></html>' #这段是你要匹配的文本
p1 = r"(?<=<h1>).+?(?=<h1>)"#这是我们写的正则表达式规则，你现在可以不理解啥意思
pattern1 = re.compile(p1)#我们在编译这段正则表达式
matcher1 = re.search(pattern1,key)#在源文本中搜索符合正则表达式的部分
print matcher1.group(0)#打印出来



key = '<div class="ds_cr"><p>根"据美国"马萨 “诸塞<p style="text-align: center;"></p>”</p><br><div id="pageurl">adad' #这段是你要匹配的文本
p1 = r'(?<=<div class="ds_cr">).+?(?=<div id="pageurl">)'#这是我们写的正则表达式规则，你现在可以不理解啥意思
pattern1 = re.compile(p1)#我们在编译这段正则表达式
matcher1 = re.search(pattern1,key)#在源文本中搜索符合正则表达式的部分
print matcher1.group(0)#打印出来
