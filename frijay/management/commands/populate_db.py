'''Populats db with all the events'''
from django.core.management.base import BaseCommand
from frijay.models import Event
from django.contrib.auth.models import User

class Command(BaseCommand):
    """Populates db with some events"""

    args = '<foo bar ...>'

    def _clear_users(self):
        users = User.objects.exclude(username="frijay")
        users.delete()

    def _clear_events(self):
        events = Event.objects.all()
        events.delete()

    def _populate_users(self):
        users = [
            {
                "username": 'jonathanrozario',  # user for debugging
                "password": "qwerty",
                "first_name": "Jonathan",
                "last_name": "Rozario",
                "email": "jonathanrozario@gmail.com"
            },
            {
                "username": 'Jack698',
                "password": "A4B2N6",
                "first_name": "Jack",
                "last_name": "Delancy",
                "email": "JD123@gmail.com"
            },
            {
                "username": 'vl02nf',
                "password": "uhiguh4th",
                "first_name": "Melissa",
                "last_name": "Khrais",
                "email": "mdlk@gmail.com"
            },
            {
                "username": 'DBL00',
                "password": "JFIEH*(ere#H",
                "first_name": "Harry",
                "last_name": "Deaplid",
                "email": "d783492@gmail.com"
            },
            {
                "username": 'Jottav',
                "password": "qwertyuiop",
                "first_name": "Gerald",
                "last_name": "Cox",
                "email": "g48fn4j@yahoo.com"
            },
            {
                "username": 'Mitchy93',
                "password": "f8hf9bf9h3ikt",
                "first_name": "Mitchall",
                "last_name": "Wallier",
                "email": "mitchy93@hotmail.com"
            },
            {
                "username": 'Firebal',
                "password": "FPSGGQQ77&",
                "first_name": "Izidor",
                "last_name": "Baum",
                "email": "ibaum002@citymail.cuny.edu"
            },
            {
                "username": 'Tsilasbury01',
                "password": "pepperegetruckleftmountain12345",
                "first_name": "Jessica",
                "last_name": "Francisco",
                "email": "j0b0ss@gmail.com"
            },
            {
                "username": 'Tklein',
                "password": "asterix",
                "first_name": "Tracy",
                "last_name": "Klein",
                "email": "tracy.klein86@yahoo.com"
            },
            {
                "username": 'talt3r',
                "password": "bombastique",
                "first_name": "frank",
                "last_name": "delgado",
                "email": "spaceys_palace@mail.com"
            },
            {
                "username": 'JessBests',
                "password": "snowden12345",
                "first_name": "Jessica",
                "last_name": "Betts",
                "email": "talthausy@mail.ru"
            },
            {
                "username": 'b0ss',
                "password": "fff@n",
                "first_name": "Joji",
                "last_name": "Miller",
                "email": "p1nkman@hotmail.com"
            }
        ]

        for user in users:
            usr = User.objects.create_user(
                user['username'],
                user['email'],
                user['password'],
                first_name=user['first_name'], last_name=user['last_name'])
            usr.save()

    def _populate_events(self):
        events = [
            {
                "title": "Friday Shabbat in Brooklyn",
                "address": "633 E 89th St",
                "address2": "Floor 3",
                "city": "Brooklyn",
                "state": "NY",
                "zipcode": "11236",
                "host": User.objects.get_by_natural_key("Mitchy93"),
                "phone": 9174741941,
                "date": "2016-12-14",
                "time1": "18:00:00",
                "time2": "20:00:00",
                "openSeats": 5,
                "additionalDetails": "COME JOIN IS IT WILL BE FUN PLEASE RESREVE "
                                     "A SEAT COME JOIN THE SHABBAT DINNER"
                                     " OF 2016"
            },
            {
                "title": "Shabbattable!",
                "address": "144 00 37th Ave",
                "address2": "Apt. 4D",
                "city": "Queens",
                "state": "NY",
                "zipcode": "11354",
                "host": User.objects.get_by_natural_key("DBL00"),
                "phone": 9174741941,
                "date": "2016-12-21",
                "time1": "19:00:00",
                "time2": "21:00:00",
                "openSeats": 2,
                "additionalDetails": "Nice family dinner with the Dieplids! We'll"
                                     " have spots for 2 people, and have a "
                                     "great time! Fresh food. Guests who arrive, "
                                     "please bring a bottle of wine."
                                     " Looking forawrd to a fun shabbat!"
            },
            {
                "title": "Dinner with the Kleins",
                "address": "15 Fort Washington Ave",
                "address2": "Apt. 2C",
                "city": "New York",
                "state": "NY",
                "zipcode": "10032",
                "host": User.objects.get_by_natural_key("Tklein"),
                "phone": 9174741941,
                "date": "2016-12-19",
                "time1": "20:00:00",
                "time2": "22:00:00",
                "openSeats": 3,
                "additionalDetails": "Good, cozy home cooked meal, games and "
                                     "dessert after :) All are welcome"
            },
            {
                "title": "Dinner with my peeps",
                "address": "225 George Washington Bridge",
                "address2": "Floor 0.5",
                "city": "Inwood",
                "state": "NY",
                "zipcode": "10045",
                "host": User.objects.get_by_natural_key("Tklein"),
                "phone": 9174741941,
                "date": "2016-12-29",
                "time1": "18:00:00",
                "time2": "22:00:00",
                "openSeats": 3,
                "additionalDetails": "Let's have shabbat!"
            },
            {
                "title": "Make Shabbat Great Again",
                "address": "17 Jackson Ave",
                "address2": "Floor B",
                "city": "Queens",
                "state": "NY",
                "zipcode": "11345",
                "host": User.objects.get_by_natural_key("Jottav"),
                "phone": 9174741941,
                "date": "2017-1-25",
                "time1": "19:30:00",
                "time2": "23:00:00",
                "openSeats": 4,
                "additionalDetails": "Because why not? Come join for festivities and "
                                     "Make Shabbat Great Again! "
                                     "Family dinner open to couples and individuals"
                                     " of all ages. We don't discrminate!"
            },
            {
                "title": "Veggies Delight",
                "address": "4225 Carle Pl.",
                "address2": "F",
                "city": "Bronx",
                "state": "NY",
                "zipcode": "15344",
                "host": User.objects.get_by_natural_key("vl02nf"),
                "phone": 9174741941,
                "date": "2017-1-25",
                "time1": "17:30:00",
                "time2": "19:00:00",
                "openSeats": 1,
                "additionalDetails": "Good vegetarian and tasty dinner! "
                                     "Homemade by everyone in the family :)"
            }
        ]

        for event in events:
            event_list = Event.objects.get_or_create(
                title=event['title'],
                address=event['address'],
                address2=event['address2'],
                city=event['city'],
                state=event['state'],
                zipcode=event['zipcode'],
                host=event['host'],
                phone=event['phone'],
                date=event['date'],
                time1=event['time1'],
                time2=event['time2'],
                openSeats=event['openSeats'],
                additionalDetails=event['additionalDetails'])[0]
            event_list.save()

    def handle(self, *args, **options):
        print("Clearing users...")
        self._clear_users()
        print("Clearing events...")
        self._clear_events()
        print("Populating users...")
        self._populate_users()
        print("Populating events...")
        self._populate_events()
