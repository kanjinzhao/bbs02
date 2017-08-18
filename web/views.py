from django.shortcuts import render

import models

# Create your views here.

def index(req):
    articles = models.Article.objects.all()
    return render(req,'index2.html',{'articles':articles})


def lanmu(req,id):

    articles = models.Article.objects.filter(categroy_id=id)

    return render(req,'index2.html',{'articles':articles})

