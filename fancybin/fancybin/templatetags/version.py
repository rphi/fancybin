from django import template
from django.utils.html import mark_safe
import fancybin
from django.conf import settings

register = template.Library()

@register.simple_tag
def APP_VERSION():
    if settings.CHANGELOGLINK:
        return mark_safe(f'{fancybin.VERSION} - <a href="{settings.CHANGELOGLINK}" target="_blank">Changelog</a>')
    return fancybin.VERSION