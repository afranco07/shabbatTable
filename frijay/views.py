'''Views for the frijay app'''
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from frijay.models import Event, Reservation
from frijay.forms import UserForm, EventForm
from frijay.twilio import send_reservation_sms


def index(request):
    """ Index Page View """
    events = Event.objects.filter(openSeats__gt=0)[:4]
    if request.method == 'POST':
        events = Event.objects.filter(city__iexact=request.POST.get('search'))
        context_dict = {'title': "Frijay!", 'Events':events}
        return render(request, 'frijay/index.html', context_dict)
    context_dict = {'title': "Frijay!", 'Events':events}
    return render(request, 'frijay/index.html', context_dict)


def about(request):
    """ About Page View """
    context_dict = {'title': "About!"}

    return render(request, 'frijay/about.html', context_dict)

def signup(request):
    """signup page view"""
    # A boolean value for telling the template
    # whether the registration was successful.
    # Set to False initially. Code changes value to
    # True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of only the UserForm
        user_form = UserForm(data=request.POST)

        # If the two forms is valid...
        if user_form.is_valid():
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Update our variable to indicate that the template
            # registration was successful.
            registered = True

        # else:
            # Invalid form or forms - mistakes or something else?
            # Print problems to the terminal.
            # print(user_form.errors)
    else:
        # Not a HTTP POST, so we render our form using two ModelForm instances.
        # These forms will be blank, ready for user input.
        user_form = UserForm()

    # Render the template depending on the context.
    return render(request, 'frijay/signup.html',
                  {'user_form': user_form,
                   'registered': registered})


def user_login(request):
    '''login page view'''
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Make a User object with Django's machinery
        user = authenticate(username=username, password=password)
        # If we have a User object, the details are correct.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            # else:
                # An inactive account was used - no logging in!
                # return HttpResponse("Your account is disabled.")

        # No user # with matching credentials was found.
        # else:
            # Bad login details were provided. So we can't log the user in.
            # print("Invalid login details: {0}, {1}".format(username, password))
            # return HttpResponse("Invalid login details supplied.")
            # The request is not a HTTP POST, so display the login form.
            # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'frijay/login.html', {})


@login_required
def user_logout(request):
    """Only logout if user is already logged in"""
    logout(request)
    # Take the user back to the homepage.
    return HttpResponseRedirect(reverse('index'))


# def profile(request):
#     '''user profile page view'''
#     context_dict = {'title': "Profile"}
#     return render(request, 'frijay/profile.html', context_dict)


# def redir(request):
#     '''redirection view'''
#     return redirect('/frijay')


def events(request):
    '''Event View'''
    all_events = Event.objects.all()
    context_dict = {'html_list': all_events}
    if request.POST.get('reserve') \
            and Event.objects.get(title=request.POST.get('reserve')).openSeats > 0:
        evnt = Event.objects.get(title=request.POST.get('reserve'))
        evnt.openSeats -= 1
        evnt.save()
        res = Reservation.objects.get_or_create(event=evnt, guest=request.user)[0]
        res.save()
        send_reservation_sms(request.user, evnt)

    return render(request, 'frijay/events.html', context_dict)


@login_required
def host_event(request):
    """View for hosting an event"""
    if request.method == 'POST':
        event_form = EventForm(data=request.POST)

        if event_form.is_valid():
            event = event_form.save(commit=False)
            event.host = request.user
            event.save()
            return HttpResponseRedirect(reverse('myevents'))
        # else:
            # invalid form or forms TODO
            # print(event.errors)
    else:
        event_form = EventForm()
    return render(request, 'frijay/host.html', {'event_form': event_form})


@login_required
def reservation(request):
    """Reservations View, Users will view their pending, accepted, and rejected
    Reservations here. They will have the ability to cancel their reservations
    if they see fit."""
    # If POST request to cancel reservation
    if request.POST.get('cancel'):
        # Fetch the event of this reservation via title
        evnt = Event.objects.get(title=request.POST.get('cancel'))
        # If the reservation was not a declined reservation (see MyEvents for details)
        if Reservation.objects.get(guest=request.user, event=evnt).accept is not False:
            # Add an open seat to the Event openSeats field
            evnt.openSeats += 1
            evnt.save()
        # Delete the reservation from the system.
        Reservation.objects.get(event=evnt, guest=request.user).delete()

    context_dict = {}
    # Get reservations where the current user is an applicant
    reservations = Reservation.objects.filter(guest=request.user)
    # Store them into a list for displaying
    context_dict['reservations'] = [x for x in reservations]
    # And send it to the renderer.
    return render(request, 'frijay/reservation.html', context_dict)


@login_required
def myevents(request):
    '''My Events page, for hosts to manage their events.
    This will allow hosts to accept or decline reservation
    requests from users.'''
    if request.method == "POST":
        # print(request.body)
        if request.POST.get('cancel'):
            Event.objects.get(title=request.POST.get('cancel')).delete()
        elif request.POST.get('approve'):
            usr = User.objects.get(username=request.POST.get('approve'))
            evnt = Event.objects.get(title=request.POST.get('event'))
            rev = Reservation.objects.get(event=evnt, guest=usr)
            rev.accept = True
            rev.save()
        elif request.POST.get('decline'):
            usr = User.objects.get(username=request.POST.get('decline'))
            evnt = Event.objects.get(title=request.POST.get('event'))
            rev = Reservation.objects.get(event=evnt, guest=usr)
            rev.accept = False
            rev.save()
            evnt.openSeats += 1
            evnt.save()

    context_dict = {}
    myevents_list = [x for x in Event.objects.all() if x.host == request.user]
    context_dict['event_list'] = []
    for event in myevents_list:
        reservations = Reservation.objects.filter(event=event)
        context_dict['event_list'].append({"event": event,
                                           "guests_u": [x.guest for x in reservations if x.accept is None],
                                           "guests_a": [x.guest for x in reservations if x.accept]
                                           })
    return render(request, 'frijay/myevents.html', context_dict)


def reservationsEvent(request, event_id):
    '''Event view for specific event'''
    eventModel = Event.objects.get(id=event_id)
    context_dict = {'event_id' : event_id,
                    'event_title' : eventModel.title,
                    'event_host' : eventModel.host.first_name + " " + eventModel.host.last_name,
                    'event_city' : eventModel.city,
                    'event_date' : eventModel.date,
                    'event_timefrom' : eventModel.time1,
                    'event_timeto' : eventModel.time2,
                    'event_seats' : eventModel.openSeats,
                    'event_details' : eventModel.additionalDetails
                   }
    return render(request, 'frijay/reservationEventPage.html', context_dict)


def howItWorks(request):
    '''howitworks page view to show user documentation'''
    context_dict = {'title': "HowItWorks"}

    return render(request, 'frijay/howItWorks.html', context_dict)