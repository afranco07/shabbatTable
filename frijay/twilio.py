"""Twilio settings for the project"""
from twilio.rest import TwilioRestClient
from twilio.rest.lookups import TwilioLookupsClient
from twilio.rest.exceptions import TwilioRestException
""" These are configuration values needed for Twilio. They shouldn't
be placed here but for purpose of functionality they are hardcoded."""
ACCOUNT_SID = "ACd56262f209cd94fe377106f857bd8f82"
AUTH_TOKEN = "2c0d255b6ad344bca74537fd5ca022c9"


def send_reservation_sms(user, event):
    """This function utilizes the Twilio SMS API to send a
    pre-formatted SMS message to a phone number given by a
    host on their event. This function takes both user and
    event object as inputs."""
    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

    phone = "+1" + str(event.phone)
    if not is_valid_number(phone):
        # For now, don't do anything.
        return
    host = event.host.first_name
    guest = user.first_name + " " + user.last_name
    email = user.email
    title = event.title
    # At this point SMS will be sent.
    client.messages.create(
        to=phone,
        from_="+16467624316",
        body=("Hi "
              + host
              + "! This is Frijay. We received a reservation request from "
              + guest
              + " ("
              + email
              + ") for your dinner event, "
              + title
              + ". Please review this request at your earliest convenience.\n"
              + "View this reservation at shabbattable.herokuapp.com/myevents/",
             )
    )


def is_valid_number(number):
    """This is a helper function that will check to see that
    the given phone number is a valid phone number. This function
    utilizes Twilio's Lookup API Client."""
    client = TwilioLookupsClient(ACCOUNT_SID, AUTH_TOKEN)
    try:
        response = client.phone_numbers.get(number, include_carrier_info=True)
        response.phone_number  # If invalid, throws an exception.
        return True
    except TwilioRestException as e:
        if e.code == 20404:
            return False
        else:
            raise e
