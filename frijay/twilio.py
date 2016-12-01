from twilio.rest import TwilioRestClient
from twilio.rest.lookups import TwilioLookupsClient
from twilio.rest.exceptions import TwilioRestException

ACCOUNT_SID = "ACd56262f209cd94fe377106f857bd8f82"
AUTH_TOKEN = "2c0d255b6ad344bca74537fd5ca022c9"

def send_reservation_sms(user,event):
    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

    phone = "+1" + str(event.phone)
    if not is_valid_number(phone):
        # For now, don't do anything.
        return
    host = event.host.first_name
    guest = user.first_name + " " + user.last_name
    email = user.email
    title = event.title

    client.messages.create(
        to=phone,
        from_="+16467624316",
        body="Hi " + host + "! This is Frijay. We received a reservation request from " + guest + " (" + email + ") for your dinner event, " + title + ". Please review this request at your earliest convenience.\nView this reservation at shabbattable.herokuapp.com/myevents/",
    )


def is_valid_number(number):
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