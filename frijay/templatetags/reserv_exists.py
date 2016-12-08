from django import template
from frijay.models import Reservation

register = template.Library()


@register.simple_tag
def reservation_exists(user, event):
    """This template tag will return a boolean value on whether a
    reservation exists for user in event. This assumes that user and
    event exists."""
    return Reservation.objects.filter(event=event, guest=user).exists
