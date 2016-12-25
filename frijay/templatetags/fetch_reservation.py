'''Class that fetches the users reservations'''
from django import template
from frijay.models import Reservation, Event

register = template.Library()


@register.simple_tag
def fetch_reservation(title, guest):
    """This function tag is used to return a reservation object given the
        title of the event and the user object. This function operates on the
        assumption that both guest and event exist in the database and that
        the guest has a reservation at the event. Logic is handled in Templating."""
    evnt = Event.objects.get(title=title)
    return Reservation.objects.get(event=evnt, guest=guest)
