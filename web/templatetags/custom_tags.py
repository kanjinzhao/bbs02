#coding=utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf8')

from django import template

register = template.Library()


def tree_search(d_dic,comment_obj):
    for k,v_dic in d_dic.items():
        if k == comment_obj.parent_comment: #找一级评论
            d_dic[k][comment_obj] = {}
            return
        else:  #找子评论
            tree_search(d_dic[k],comment_obj)



def make_html(son_comment_dic,margin_val):
    html =""
    for k,v_dic in son_comment_dic.items():

        user = str(k.user)

        html += "<div style='margin-left:%spx;margin-top:5px;' class='position--genuine featured-sign'>" % margin_val +"<span>" + user + ":</span>" + k.comment +"<a href='' class='huifu'>回复</a>" + "</div>"

        if v_dic:
            html += make_html(v_dic,margin_val+15)
    return html


@register.simple_tag()


def build_comment_tree(comment_list):

    #print ("comment_list:",comment_list)

    comment_dic ={}

    for comment_obj in comment_list:
        if comment_obj.parent_comment is None: #没有父评论
            comment_dic[comment_obj] = {}
        else:  #有父评论
            tree_search(comment_dic,comment_obj)
    #评论树完成


    #输出html

    html = "<div class='comment'>"

    margin_lef = 0

    for k,v in comment_dic.items():

        user = str(k.user)
        datetime = str(k.date)


        html += "<div class='position position--genuine featured-sign position--featured'>" + "<span class='commuser'>" + user + ":</span>" + k.comment + "<span class='commtime'>"+ datetime +"</span>" +"<a href='' class='huifu'>回复</a>"  +"</div>"
        html += make_html(v,margin_lef+15)

    html += "</div>"

    return html