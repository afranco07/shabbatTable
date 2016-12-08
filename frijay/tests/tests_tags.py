from django.template import Template, Context
from django.test import Client, TestCase
from django.contrib.auth.models import User
from frijay.models import Event, Reservation

class TemplateTagTest(TestCase):

    TEMPLATE1 = Template("{% load fetch_reservation %} {% fetch_reservation event user as res %} {{ res.guest }} <br> {{ res.event }} <br> {{ res.accept }}")
    TEMPLATE2 = Template("{% load is_host %} {% is_host event user as host %} {{ host }}")
    TEMPLATE3 = Template("{% load reserv_exists %} {% reservation_exists user event as exists %} {{ exists }}")

    def setUp(self):
        self.user = User.objects.create(username="user1")
        self.host = User.objects.create(username="host1")
        self.event1 = Event.objects.create(
            title='Shabbat',
            address='testaddress',
            city='Brooklyn',
            state='New York',
            phone='1231231234',
            date='2016-12-07',
            time1='03:24:12',
            time2="03:24:12",
            openSeats='10',
            additionalDetails='None',
            host=self.host,
        )
        self.reservation = Reservation.objects.create(event=self.event1, guest = self.user)

    def test_reservation_fetch(self):
        rendered = self.TEMPLATE1.render(Context({'user':self.user, 'event':self.event1.title}))
        self.assertIn(self.user.username, rendered)
        self.assertIn(self.event1.title, rendered)
        self.assertIn(str(self.reservation.accept), rendered)

    def test_is_host(self):
        rendered = self.TEMPLATE2.render(Context({'user':self.user, 'event':self.event1.title}))
        self.assertIn("False", rendered)
        rendered = self.TEMPLATE2.render(Context({'user': self.host, 'event': self.event1.title}))
        self.assertIn("True", rendered)

    def test_reserv_exists(self):
        rendered = self.TEMPLATE3.render(Context({'user': self.user, 'event': self.event1}))
        self.assertIn("True", rendered)
        rendered = self.TEMPLATE3.render(Context({'user':self.host, 'event':self.event1}))
        self.assertIn("False", rendered)