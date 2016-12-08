from django import template
from frijay.models import Event

register = template.Library()


@register.simple_tag
def is_host(title, user):
    """ This template tag function returns a boolean on whether
     or not a user is currently a host of any event that exists on
     the website. This assumes that user exists."""
    return Event.objects.filter(title=title, host=user).exists
