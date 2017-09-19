#coding=utf-8
# @Time    : 17-9-19 下午2:29
# @Author  : LIUMINGBO
# @Email   : 540032146@qq.com
from models import Article
from haystack import indexes


class BlogIndex(indexes.SearchIndex, indexes.Indexable):

    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Article

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()  # 确定在建立索引时有些记录被索引，这里我们简单地返回所有记录