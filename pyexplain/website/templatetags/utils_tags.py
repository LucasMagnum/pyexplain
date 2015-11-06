# coding: utf-8

from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter(name='to_html')
def to_html(value):
    return mark_safe(value.replace('\n', '<br>').replace('\r', '').strip())


@register.filter(name='meta')
def meta(object, attr):
    return getattr(object._meta, attr)
