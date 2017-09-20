#coding=utf-8

from django.shortcuts import render,HttpResponseRedirect,render_to_response,RequestContext
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import logout,login,authenticate
from forms import ArticleForm,CommentForm,RegistForm,SearchForm
#注册时导入User表
from django.contrib.auth.models import User
#引入分页
from django.core.paginator import Paginator,PageNotAnInteger, EmptyPage

#引入jieba分词
from jieba import analyse

#引入自定义文件
import mvhtml

import models
from django.db.models import Q



def my_pagination(request, queryset, display_amount=15, after_range_num = 5,bevor_range_num = 4):
    #按参数分页
    paginator = Paginator(queryset, display_amount)
    try:
        #得到request中的page参数
        page =int(request.GET.get('page'))
    except:
        #默认为1
        page = 1
    try:
        #尝试获得分页列表
        objects = paginator.page(page)
    #如果页数不存在
    except EmptyPage:        #获得最后一页
        objects = paginator.page(paginator.num_pages)
    #如果不是一个整数
    except:
        #获得第一页
        objects = paginator.page(1)
    #根据参数配置导航显示范围
    if page >= after_range_num:
        page_range = paginator.page_range[page-after_range_num:page+bevor_range_num]
    else:
        page_range = paginator.page_range[0:page+bevor_range_num]
    return objects,page_range




#提取关键词
def show_tag(id):
    tags = models.Tags.objects.all().order_by("-num")[0:id]
    return tags

#推荐相关文章
def like_art(keywords0,keywords1,keywords2,num):
    like_arts = models.Article.objects.filter(Q(title__contains=keywords0)|Q(title__contains=keywords1)|Q(title__contains=keywords2))[0:num]
    return like_arts

#获取最新文章列表
def newart_list(num):
    last_list = models.Article.objects.all().order_by("-publish_date")[0:num]
    return last_list






# Create your views here.

def index(req):
    articles = models.Article.objects.all().order_by("-publish_date")[0:20]
    for article in articles:
        strs = str(article.head_img)
        if 'static/uploads' in strs:
            article.head_img = '/'+ str(article.head_img)
        #拆分关键字
        keywords = article.keywords
        if keywords is not None:
            article.keywords = keywords.split(',')
    return render(req,'index.html',{'articles':articles})


def lanmu(req,id):

    articles = models.Article.objects.filter(categroy_id=id).order_by("-publish_date")
    #for article in articles:
    #    keywords = article.keywords
    #    if keywords is not None:
    #        article.keywords = keywords.split(',')

    #    strs = str(article.head_img)
    #    if 'static/uploads' in strs:
    #        article.head_img = '/'+ str(article.head_img)
    #    #拆分关键字

    objects, page_range = my_pagination(req, articles)

    #栏目名称
    category = models.Category.objects.get(id=id)


    #获取15个标签词
    tags = show_tag(15)

    #获取最新文章10条
    last_list = newart_list(10)

    #return render(req,'index.html',{'articles':articles,'page_range':page_range})
    return render_to_response('list.html',{'articles':objects,'cagegory':category,'page_range':page_range,'tags':tags,'last_list':last_list},context_instance=RequestContext(req))

def article(req,id):

    errs=''
    #提交评论
    if req.method == "POST":
        form = CommentForm(req.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            form_data['user_id'] = req.user.userprofile.id
            form_data['article_id'] = id
            form_data['parent_comment_id'] = req.POST.get('fatherid')
            #print form_data
            new_comment_obj = models.Comment(**form_data)
            new_comment_obj.save()
        else:
            errs='请填写评论内容'

    try:
        artilce = models.Article.objects.get(id=id)
        author = models.UserProfile.objects.get(id=artilce.author_id)

        #拆分关键字
        keywords = artilce.keywords
        if keywords is not None:
            keyword = keywords.split(',')
        else:
            keyword=''
        #print keyword


        #获取评论数
        comment = models.Comment.objects.filter(article_id=id)
        #print comment
        sum_com =len(comment)

    except ObjectDoesNotExist as e:

        return render(req,'404.html',{'msg':u'文章不存在！'})

    #获取15个标签词
    tags = show_tag(15)

    #查找5篇相关文章
    like_arts =like_art(keyword[0],keyword[1],keyword[2],5)

    #获取最新文章10条
    last_list = newart_list(10)


    return render(req,'art.html',{'article':artilce,'author':author,'errs':errs,'sum_com':sum_com,'keywords':keyword,'tags':tags,'like_arts':like_arts,'last_list':last_list})





def log_out(request):
    logout(request)
    return HttpResponseRedirect('/')

def log_in(req):

    err_msg = ""

    if req.method == "POST":
       # print ('user login')
        username = req.POST.get('username')
        password = req.POST.get('password')
        user = authenticate(username = username,password = password)
        if user is not None:
            login(req,user)
            return HttpResponseRedirect('/')
        else:
            err_msg = "用户名或者密码错误"

    return render(req,'login.html',{'err_msg':err_msg})

#发帖
def add_art(req):
    errs=''

    if req.method == "POST":
        #print(req.POST)
        form = ArticleForm(req.POST,req.FILES)
        if form.is_valid():
            #print ("--form data:",form.cleaned_data)
            form_data = form.cleaned_data
            form_data['author_id'] = req.user.userprofile.id
            #jieba 自动从title提取关键词,
            textrank = analyse.textrank
            keywords = textrank(form_data['title'])
            #循环组合前3个关键词
            arr = []
            n=0
            for s in keywords:
                arr.append(s)
                strs = ','.join(arr)
                form_data['keywords'] = strs

                # 循环保存到tags表
                #查询数据库tag是否存在
                try:
                    have_tag=models.Tags.objects.get(tagname=s)
                    num = int(have_tag.num) + 1
                    models.Tags.objects.filter(tagname=s).update(num=num)
                except:
                    b = models.Tags(tagname=s, num=1)
                    b.save()
                n=n+1
                if n==3:
                    break

            #增加文章描述
            description = form_data['content']

            form_data['description'] =mvhtml.strip_tags(description[0:200])


            new_article_obj = models.Article(**form_data)
            new_article_obj.save()
            return render(req,'addarticle.html')
        else:
            #print ('err:',form.errors)
            errs = form.errors


    if req.user.userprofile.id:
        category = models.Category.objects.all()
        return render(req,'addarticle.html',{'category':category,'errs':errs})

#用户注册验证
def register(req):
    errs =''
    if req.method=="POST":
        form = RegistForm(req.POST,req.FILES)
        if form.is_valid():
            #user表 注册
            form_data= form.cleaned_data
            username=form_data['username']
            isname = models.User.objects.filter(username=username)
            if len(isname)>0:
                username=str(username)
                errs="用户名 "+ username +" 已存在"
                return render(req, 'register.html', {'err_userame': errs})

            password=form_data['password']
            repassword=form_data['repassword']

            if password != repassword:
                errs = "两次输入密码不一致"
                return render(req, 'register.html', {'err_password': errs})

            email=form_data['email']
            user = User.objects.create_user(username,email,password)
            user.save()

            #UserProfile表增加 昵称
            userprofile = models.UserProfile()
            userprofile.name = form_data['name']
            userprofile.user_id = user.id
            userprofile.save()
            ok_msg = "注册成功，马上登录"
            return render(req, 'login.html', {'ok': ok_msg,'username':username})
        else:
            errs = form.errors
    return render(req,'register.html',{'err_msg':errs})


#关键字标签
def tags(req,tag):
    list = models.Article.objects.filter(keywords__contains=tag).order_by("-publish_date")
    for article in list:
        strs = str(article.head_img)
        if 'static/uploads' in strs:
            article.head_img = '/'+ str(article.head_img)
    objects, page_range = my_pagination(req, list)

    return render(req,'search.html',{'tag':tag,'list':objects,'page_range':page_range},context_instance=RequestContext(req))



#全站搜索
def searchart(req):
    if req.method =="POST":
        form = SearchForm(req.POST)
        if form.is_valid():
            form_data= form.cleaned_data
            keywords = form_data['keyword']

            list = models.Article.objects.filter(title__contains=keywords).order_by("-publish_date")
            for article in list:
                strs = str(article.head_img)
                if 'static/uploads' in strs:
                    article.head_img = '/'+ str(article.head_img)
            objects, page_range = my_pagination(req, list)
        else:
            return HttpResponseRedirect('/')

    #列表页推荐标签
    tag = show_tag(20)

    return render(req,'search.html',{'tag':keywords,'list':objects,'page_range':page_range,'tags':tag},context_instance=RequestContext(req))
