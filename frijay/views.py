'''Views for the frijay app'''

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Event
from django.template import loader


def index(request):
    '''index page view
    Construct a dictionary to pass to the template engine as its context.
    Note the key title is the same as {{ title }} in the template!

    Return a rendered response to send to the client.
    Shortcut function 'render()' is used to make coding simpler.
    Note that the first parameter is the template we wish to use.
    '''
    context_dict = {'title': "Frijay!"}
    return render(request, 'frijay/index.html', context_dict)


def about(request):
    '''request page view'''
    context_dict = {'title': "About!"}

    return render(request, 'frijay/about.html', context_dict)


def signup(request):
    '''signup page view'''
    context_dict = {'title': "Signup"}
    return render(request, 'frijay/signup.html', context_dict)


def login(request):
    '''login page view'''
    context_dict = {'title': "Login"}
    return render(request, 'frijay/login.html', context_dict)


def profile(request):
    '''user profile page view'''
    context_dict = {'title': "Profile"}
    return render(request, 'frijay/profile.html', context_dict)


def redir(request):
    '''redirection view'''
    return redirect('/frijay')

def events(request):
    '''Event View'''
    all_events = Event.objects.all()
    html = ''

    for event in all_events:
        url = '/frijay/events/' + str(event.id) + '/'
        html += '<a href="' + url + '">' + event.title + '</a><br>'
    context_dict = {'html_list' : html}

    return render(request, 'frijay/events.html', context_dict)

def reservationsEvent(request, event_id):
    '''Event view for specific event'''
    eventModel = Event.objects.get(id = event_id)
    context_dict = {'event_id' : event_id,
                    'event_title' : eventModel.title,
                    'event_host' : eventModel.host,
                    'event_address' : eventModel.address,
                    'event_date' : eventModel.date,
                    'event_time' : eventModel.time,
                    'event_seats' : eventModel.openSeats,
                    'event_details' : eventModel.additionalDetails
                    }
    return render(request, 'frijay/reservationEventPage.html',context_dict)