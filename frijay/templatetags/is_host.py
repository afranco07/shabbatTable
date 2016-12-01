from django import template
from frijay.models import Event

register = template.Library()


@register.simple_tag
def is_host(title, user):
    return Event.objects.filter(title=title, host=user).exists
