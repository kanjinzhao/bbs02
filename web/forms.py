#coding=utf-8
from django import forms

class ArticleForm(forms.Form):
    title = forms.CharField(max_length=255,min_length=5)
    categroy_id = forms.CharField()
    head_img = forms.ImageField()
    content = forms.CharField(max_length=5000,min_length=10)



class CommentForm(forms.Form):
    comment = forms.CharField(max_length=2000,min_length=2)


class RegistForm(forms.Form):
    username = forms.CharField(max_length=50,min_length=3)
    name = forms.CharField(max_length=50,min_length=1)
    email = forms.EmailField()
    password = forms.CharField()
    repassword = forms.CharField()

class SearchForm(forms.Form):
    keyword = forms.CharField(min_length=1)