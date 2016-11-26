import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shabbattable.settings.dev')
# NOTE THIS ONLY WORKS FOR DEV, NOT PROD.
import django

django.setup()
from frijay.models import Event, Reservation
from django.contrib.auth.models import User


def populate():
    """First, we will create lists of dictionaries containing the
    pages we want to add into each category.
    Then we will create a dictionary of dictionaries for our categories.
    This might seem a little bit confusing, but it allows us to iterate
    through each data structure, and add the data to our models.
    """
    users = [
                {
                    "username": 'user1',
                    "password": "passwordlol",
                    "first_name":"Jack",
                    "last_name":"Bauer",
                    "email":"lol@gmail.com"
                },
                {
                    "username": 'vl02nf',
                    "password": "passwefuhiguh4th",
                    "first_name": "Melissa",
                    "last_name": "Khrais",
                    "email": "mdlol@gmail.com"
                },
                {
                    "username": 'DBL00',
                    "password": "JFIEH*(#H",
                    "first_name": "Hoss",
                    "last_name": "Deapld",
                    "email": "d783492@gmail.com"
                }
            ]


    """ If you want to add more categories or pages, add them
    to the dictionary above.

    The code below goes through the cats dictionary, then adds each
    category, and then adds all the associated pages for that category.

    """

    for u in users:
        add_user(u)



def add_user(u):
    usr = User.objects.get_or_create(username=u['username'], password=User.set_password(User,u['password']) first_name=u['first_name'], last_name=u['last_name'], email=u['email'])[0]
    usr.save()
    return u



# Start execution here!
if __name__ == '__main__':
    print("Starting Frijay population script...")
    populate()















