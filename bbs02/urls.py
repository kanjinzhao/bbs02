"""bbs02 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

from web import views
from web import tests

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',views.index,name='index'),
    url(r'^category/(\d+)/$',views.lanmu,name='lanmu'),
    url(r'^article/(\d+)/$', views.article, name='article'),
    url(r'^user/logout/',views.log_out,name='logout'),
    url(r'^user/login/',views.log_in,name='login'),
    url(r'^user/addart/',views.add_art,name='addart'),
    url(r'^user/register/',views.register,name='register'),
    url(r'^tags/(.*)',views.tags,name='tags'),
    url(r'^test/',views.test),

]
