'''Views for the frijay app'''

from django.shortcuts import render, redirect
from django.http import HttpResponse


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
    '''Reservations View'''
    return render(request, 'frijay/events.html')

def reservationsEvent(request, event_id):
    '''Reservations view for specific event'''
    return HttpResponse("<h2>Details for event id " + str(event_id) + "</h2>")