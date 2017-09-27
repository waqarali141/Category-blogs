__author__ = 'waqarali'
from django import template
register = template.Library()


@register.inclusion_tag('blogs/page_header.html')
def logged_in_user(user, takes_context=True):
    return {'user': user}