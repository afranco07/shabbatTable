from django import template
from frijay.models import Reservation

register = template.Library()


@register.simple_tag
def reservation_exists(user, event):
    return Reservation.objects.filter(event=event, guest=user).exists
