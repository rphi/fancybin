from os.path import exists
from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.simple_tag
def TRACKING_CODE():
  if exists('./TRACKING.html'):
    with open('./TRACKING.html', 'r') as v:
      return mark_safe(v.read())
  return ''