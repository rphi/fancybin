from django import template
from notices.models import Notice
from django.db.models import Q
from django.utils import timezone

register = template.Library()

@register.inclusion_tag('www/notices.html', takes_context=True)
def notices(context):
    notices = Notice.objects.filter(
        Q(visible=True) &
        Q(Q(expires__gte=timezone.now()) | Q(expires__isnull=True)) &
        Q(Q(target__in=context['user'].groups.all()) | Q(target__isnull=True))
    ).order_by('priority', '-timestamp')

    return {
        'notices': notices
        }