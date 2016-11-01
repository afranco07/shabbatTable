from django.shortcuts import render, redirect


# Create your views here.

def index(request):
    # Construct a dictionary to pass to the template engine as its context.
    # Note the key title is the same as {{ title }} in the template!

    context_dict = {'title': "Frijay!"}

    # Return a rendered response to send to the client. We make use of the shortcut
    # function to make our lives easier. Note that the first parameter
    # is the template we wish to use.

    return render(request, 'frijay/index.html', context_dict)


def about(request):
    context_dict = {'title': "About!"}

    return render(request, 'frijay/about.html', context_dict)

def about(request):
    context_dict = {'title': "Signup"}

    return render(request, 'frijay/signup.html', context_dict)

def about(request):   
    context_dict = {'title': "Login"}

    return render(request, 'frijay/login.html', context_dict)

def about(request):   
    context_dict = {'title': "Profile"}

    return render(request, 'frijay/profile.html', context_dict)

def redir(request):
    return redirect('/frijay')
