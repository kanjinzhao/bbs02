#coding=utf-8
from django.contrib import admin
import models
# Register your models here.


#自定义后台栏目列表显示项
class CategroyAdmin(admin.ModelAdmin):
    list_display =('id','name')


#自定义后台文章列表显示项
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id','title','categroy','author_id','publish_date','hideden')



#自定义userProfile列表项
class UserprofileAdmin(admin.ModelAdmin):
    list_display = ('name','get_user_article')

    def get_user_article(self,user_id):
        num = models.Article.objects.filter(author_id=user_id)
        return len(num)

    get_user_article.short_description = u'发贴数'


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id','comment','user_id','date')

class TagsAadmin(admin.ModelAdmin):
    list_display = ('id','tagname','num','update_time')


admin.site.register(models.Article,ArticleAdmin)
admin.site.register(models.UserGroup)
admin.site.register(models.Category,CategroyAdmin)
admin.site.register(models.ThumUp)
admin.site.register(models.UserProfile,UserprofileAdmin)
admin.site.register(models.Comment,CommentAdmin)
admin.site.register(models.Tags,TagsAadmin)

