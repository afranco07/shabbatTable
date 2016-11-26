from django.core.management.base import BaseCommand
from frijay.models import Event, Reservation
from django.contrib.auth.models import User


class Command(BaseCommand):
    args = '<foo bar ...>'
    help = 'our help string comes here'



    def _clear_users(self):
        users = User.objects.exclude(username="frijay")
        users.delete()


    def __clear_events(self):
        events = Event.objects.all()
        events.delete()


    def _populate_users(self):
        users = [
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
            }
        ]

        for u in users:
            usr = User.objects.create_user(u['username'], u['email'], u['password'], first_name=u['first_name'],
                                           last_name=u['last_name'])
            usr.save()

    def _populate_events(self):
        events = [
            {
                "title": "Friday Shabbat in Brooklyn",
                "address": "633 E 89th St, Brooklyn, NY 11236",
                "host": User.objects.get_by_natural_key("Mitchy93"),
                "date": "2016-12-14",
                "time": "18:00:00",
                "openSeats": 5,
                "additionalDetails": "COME JOIN IS IT WILL BE FUN PLEASE RESREVE A SEAT COME JOIN THE SHABBAT DINNER OF 2016"
            },
            {
                "title": "Shabbattable!",
                "address": "144 00 37th Ave, Queens, NY, 11354",
                "host": User.objects.get_by_natural_key("DBL00"),
                "date": "2016-12-21",
                "time": "19:00:00",
                "openSeats": 2,
                "additionalDetails": "Nice family dinner with the Dieplids! We'll have spots for 2 people, and have a great time! Fresh food. Guests who arrive, please bring a bottle of wine. Looking forawrd to a fun shabbat!"
            }
        ]

        for e in events:
            c = Event.objects.get_or_create(title=e['title'], address=e['address'], host=e['host'], date=e['date'],
                                            time=e['time'], openSeats=e['openSeats'],
                                            additionalDetails=e['additionalDetails'])[0]
            c.save()

    def handle(self, *args, **options):
        print("Clearing users...")
        self._clear_users()
        print("Clearing events...")
        self.__clear_events()
        print("Populating users...")
        self._populate_users()
        print("Populating events...")
        self._populate_events()
