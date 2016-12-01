from django import template
from frijay.models import Reservation, Event

register = template.Library()


@register.simple_tag
def fetch_reservation(title, guest):
    evnt = Event.objects.get(title=title)
    return Reservation.objects.get(event=evnt, guest=guest)
