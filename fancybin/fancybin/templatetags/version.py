from django import template
import fancybin

register = template.Library()

@register.simple_tag
def APP_VERSION():
    return fancybin.VERSION