#coding=utf-8
from django.contrib import admin
import models
# Register your models here.


#自定义后台栏目列表显示项
class CategroyAdmin(admin.ModelAdmin):
    list_display =('id','name')


#自定义后台文章列表显示项
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id','title','categroy','publish_date','hideden')



admin.site.register(models.Article,ArticleAdmin)
admin.site.register(models.UserGroup)
admin.site.register(models.Category,CategroyAdmin)
admin.site.register(models.ThumUp)
admin.site.register(models.UserProfile)
admin.site.register(models.Comment)
