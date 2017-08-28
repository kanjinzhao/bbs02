from django import template

register = template.Library()


@register.simple_tag()

def build_comment_tree(comment_list):

    print ("comment_list:",comment_list)