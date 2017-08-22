#coding=utf-8

from django.shortcuts import render,HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import logout,login,authenticate
from forms import ArticleForm


import models

# Create your views here.

def index(req):
    articles = models.Article.objects.all()
    return render(req,'index.html',{'articles':articles})


def lanmu(req,id):

    articles = models.Article.objects.filter(categroy_id=id)

    return render(req,'index.html',{'articles':articles})

def article(req,id):

    try:
        artilce = models.Article.objects.get(id=id)
        author  = models.UserProfile.objects.get(id=artilce.author_id)

    except ObjectDoesNotExist as e:

        return render(req,'404.html',{'msg':u'文章不存在！'})

    return render(req,'art.html',{'article':artilce,'author':author})

def log_out(request):
    logout(request)
    return HttpResponseRedirect('/')

def log_in(req):

    err_msg = ""

    if req.method == "POST":
        print ('user login')
        username = req.POST.get('username')
        password = req.POST.get('password')
        user = authenticate(username = username,password = password)
        if user is not None:
            login(req,user)
            return HttpResponseRedirect('/')
        else:
            err_msg = "用户名或者密码错误"

    return render(req,'login.html',{'err_msg':err_msg})

def add_art(req):
    errs=''

    if req.method == "POST":
        print(req.POST)
        form = ArticleForm(req.POST,req.FILES)
        if form.is_valid():
            #print ("--form data:",form.cleaned_data)
            form_data = form.cleaned_data
            form_data['author_id'] = req.user.userprofile.id
            new_article_obj = models.Article(**form_data)
            new_article_obj.save()
            return render(req,'addarticle.html')
        else:
            #print ('err:',form.errors)
            errs = form.errors


    if req.user.userprofile.id:
        category = models.Category.objects.all()
        return render(req,'addarticle.html',{'category':category,'errs':errs})