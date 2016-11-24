'''Views for the frijay app'''
from django.shortcuts import render, redirect
from frijay.forms import UserForm, UserProfileForm
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
    '''about page view'''
    context_dict = {'title': "About!"}

    return render(request, 'frijay/about.html', context_dict)


def signup(request):
    '''signup page view'''
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
        profile_form = UserProfileForm(data=request.POST)

        # If the two forms is valid...
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves,
            # we set commit=False. This delays saving the model
            # until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user

            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and
            # put it in the UserProfile model.
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            # Now we save the UserProfile model instance.
            profile.save()

             # Update our variable to indicate that the template
             # registration was successful.
            registered = True

        else:
            # Invalid form or forms - mistakes or something else?
            # Print problems to the terminal.
            print(user_form.errors, profile_form.errors)
    else:
        # Not a HTTP POST, so we render our form using two ModelForm instances. # These forms will be blank, ready for user input.
        user_form = UserForm()
        profile_form = UserProfileForm()

    # Render the template depending on the context.
    return render(request, 'frijay/signup.html',
                  {'user_form': user_form,
                   'profile_form': profile_form,
                   'registered': registered})


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
