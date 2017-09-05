#coding=utf-8

from django.shortcuts import render,HttpResponseRedirect,render_to_response,RequestContext
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import logout,login,authenticate
from forms import ArticleForm,CommentForm,RegistForm
#注册时导入User表
from django.contrib.auth.models import User
#引入分页
from django.core.paginator import Paginator,PageNotAnInteger, EmptyPage

#引入jieba分词
from jieba import analyse

import models


def my_pagination(request, queryset, display_amount=8, after_range_num = 5,bevor_range_num = 4):
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





# Create your views here.

def index(req):
    articles = models.Article.objects.all()
    return render(req,'index.html',{'articles':articles})


def lanmu(req,id):

    articles = models.Article.objects.filter(categroy_id=id)
    objects, page_range = my_pagination(req, articles)
    #return render(req,'index.html',{'articles':articles,'page_range':page_range})
    return render_to_response('list.html',{'articles':objects,'page_range':page_range},context_instance=RequestContext(req))

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
        keyword = keywords.split(',')
        #print keyword


        #获取评论数
        comment = models.Comment.objects.filter(article_id=id)
        #print comment
        sum_com =len(comment)

    except ObjectDoesNotExist as e:

        return render(req,'404.html',{'msg':u'文章不存在！'})

    return render(req,'art.html',{'article':artilce,'author':author,'errs':errs,'sum_com':sum_com,'keywords':keyword})





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
                n=n+1
                arr.append(s)
                if n==3:
                    break
            strs = ','.join(arr)
            form_data['keywords'] =strs

            #增加文章描述
            description = form_data['content']
            form_data['description'] = description[0:200]


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
    list = models.Article.objects.filter(keywords__contains=tag)
    objects, page_range = my_pagination(req, list)

    return render(req,'search.html',{'tag':tag,'list':objects,'page_range':page_range},context_instance=RequestContext(req))
