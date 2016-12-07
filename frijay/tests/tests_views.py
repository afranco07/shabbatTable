from django.test import TestCase
from django.contrib.auth import get_user_model
from frijay.models import Event
from django.contrib.auth.models import User
from django.test import Client

class ViewsTest(TestCase):

    '''Creates the User, and tests if they can login'''
    def setUp(self):
        user = User.objects.create_user('bob', '', 'temp')
        user.set_password('temp')
        self.client.login(username='bob', password='temp')
        self.assertTrue(user.is_authenticated())

    '''Test the index.html page'''
    def test_indexPage(self):
        """Tests the landing page"""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    '''Test the reservation.html page'''
    def test_reservationPage(self):
        """Tests the reservations page """
        self.client.login(username='bob', password='temp')
        response = self.client.get("/reservations/")
        self.assertEqual(response.status_code, 200)

    '''Test the events.html page'''
    def test_eventsPage(self):
        """Tests the events page"""
        response = self.client.get("/events/")
        self.assertEqual(response.status_code, 200)

    '''Test the about.html page'''
    def test_aboutPage(self):
        """Tests the about page"""
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)

    '''Test the login.html page'''
    def test_loginPage(self):
        """Tests the login page"""
        response = self.client.get("/login/")
        self.assertEqual(response.status_code, 200)

    '''Test the signup.html'''
    def test_signUpPage(self):
        """Tests the signup page"""
        response = self.client.get("/signup/")
        self.assertEqual(response.status_code, 200)

    '''Tests the host.html page'''

    def test_hostDinner(self):
        self.client.login(username='bob', password='temp')
        response = self.client.get("/host/")
        self.assertEqual(response.status_code, 200)

    '''Test the myevents.html'''

    def test_reservations(self):
        self.client.login(username='bob', password='temp')
        response = self.client.get("/myevents/")
        self.assertEqual(response.status_code, 200)


    """Test whether our events show up on the homepage"""
    '''Adding one event and testing whether it will show up on the featured events on index page'''
    def test_one_event(self):
        Event.objects.create(title='Shabbat',address='testaddress',city='Brooklyn',state='New York',
                             phone='1231231234',date='2016-12-07',time1='03:24:12',time2="03:24:12",
                             openSeats='10',additionalDetails='None')
        response = self.client.get('/')
        self.assertContains(response, 'Shabbat')
        self.assertContains(response, 'Brooklyn')
        self.assertContains(response, '10')

    '''Adding two events and testing whether they will show up on the featured events on index page'''
    def test_two_events(self):
        Event.objects.create(title='Frijay', address='testaddress2', city='Queens', state='New York',
                             phone='1233213221', date='2016-12-07', time1='03:24:12', time2="03:24:12",
                             openSeats='2', additionalDetails='None')
        Event.objects.create(title='Shabbat', address='testaddress', city='Brooklyn', state='New York',
                             phone='1231231234', date='2016-12-07', time1='03:24:12', time2="03:24:12",
                             openSeats='10', additionalDetails='None')
        response = self.client.get('/')
        self.assertContains(response, 'Frijay')
        self.assertContains(response, 'Queens')
        self.assertContains(response, '2')

    '''Testing will the output print statment will show up upon no events in the database'''
    def test_no_events(self):
        response = self.client.get('/')
        self.assertContains(response, 'Sorry, no events right now :( Please come back later.')

    '''Test whether events show up on Events page'''

    '''Adding one event and testing whether it will show up on the events page'''
    def test_one_event_eventpage(self):
        Event.objects.create(title='Shabbat', address='testaddress', city='Brooklyn', state='New York',
                             phone='1231231234', date='2016-12-07', time1='03:24:12', time2="03:24:12",
                             openSeats='10', additionalDetails='None')
        response = self.client.get('/events/')
        self.assertContains(response, 'Shabbat')
        self.assertContains(response, 'Brooklyn')
        self.assertContains(response, '10')

    '''Testing the events page on no events in Database'''
    def test_no_events_eventspage(self):
        response = self.client.get('/events/')
        self.assertContains(response, 'Sorry, no events right now :( Please come back later.')


