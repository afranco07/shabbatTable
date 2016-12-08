"""Tests for the views"""
from django.test import TestCase
from frijay.models import Event
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.contrib.auth import get_user_model

class ViewsTest(TestCase):
    '''Creates the User, and tests if they can login'''

    def setUp(self):
        user = User.objects.create_user('bob', '', 'temp')
        user.set_password('temp')
        self.client.login(username='bob', password='temp')
        self.assertTrue(user.is_authenticated())

    def test_landing_page(self):
        """Tests the landing page"""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        searchresponse = self.client.post('/', {'search': 'queens'})
        self.assertEqual(searchresponse.status_code, 200)

    def test_reservation_page(self):
        """Tests the reservations page """
        self.client.login(username='bob', password='temp')
        response = self.client.get("/reservations/")
        self.assertEqual(response.status_code, 200)

    def test_events_page(self):
        """Tests the events page"""
        response = self.client.get(reverse('events'))
        self.assertEqual(response.status_code, 200)

    def test_about_page(self):
        """Tests the about page"""
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)

    def test_login_page(self):
        """Tests the login page"""
        response = self.client.get("/login/")
        self.assertEqual(response.status_code, 200)

    def test_signup_page(self):
        """Tests the signup page"""
        response = self.client.get("/signup/")
        self.assertEqual(response.status_code, 200)
        data = {'first_name': "bob",
                'last_name': "franklin",
                'username': "bobf",
                'email': "bob@mail.com",
                'password': "temp"}

        formresponse = self.client.post('/signup/', data)
        self.assertEqual(formresponse.status_code, 200)
        # self.assertTrue(form.is_valid())

    def test_host_dinner(self):
        """Tests the host.html page"""
        self.client.login(username='bob', password='temp')
        response = self.client.get("/host/")
        self.assertEqual(response.status_code, 200)

    def test_reservations(self):
        """Test the myevents.html"""
        self.client.login(username='bob', password='temp')
        response = self.client.get("/myevents/")
        self.assertEqual(response.status_code, 200)

    def test_how_it_works(self):
        """Tests the howitworks page"""
        response = self.client.get("/howitworks/")
        self.assertEqual(response.status_code, 200)



    def test_one_event(self):
        """Adding one event and testing whether it will show up
            on the featured events on index page"""
        Event.objects.create(title='Shabbat', address='testaddress',
                             city='Brooklyn', state='New York',
                             phone='1231231234', date='2016-12-07',
                             time1='03:24:12', time2="03:24:12",
                             openSeats='10', additionalDetails='None')
        response = self.client.get('/')
        self.assertContains(response, 'Shabbat')
        self.assertContains(response, 'Brooklyn')
        self.assertContains(response, '10')

    def test_two_events(self):
        """Adding two events and testing whether they will show up
            on the featured events on index page"""
        Event.objects.create(title='Frijay', address='testaddress2',
                             city='Queens', state='New York',
                             phone='1233213221', date='2016-12-07',
                             time1='03:24:12', time2="03:24:12",
                             openSeats='2', additionalDetails='None')
        Event.objects.create(title='Shabbat', address='testaddress',
                             city='Brooklyn', state='New York',
                             phone='1231231234', date='2016-12-07',
                             time1='03:24:12', time2="03:24:12",
                             openSeats='10', additionalDetails='None')
        response = self.client.get('/')
        self.assertContains(response, 'Frijay')
        self.assertContains(response, 'Queens')
        self.assertContains(response, '2')

    def test_no_events(self):
        """Testing will the output print statment will show up upon
            no events in the database"""
        response = self.client.get('/')
        self.assertContains(response, 'Sorry, no events right now :( Please come back later.')

    def test_one_event_eventpage(self):
        """Adding one event and testing whether it will show up on the events page"""
        Event.objects.create(title='Shabbat', address='testaddress',
                             city='Brooklyn', state='New York',
                             phone='1231231234', date='2016-12-07',
                             time1='03:24:12', time2="03:24:12",
                             openSeats='10', additionalDetails='None')
        response = self.client.get('/events/')
        self.assertContains(response, 'Shabbat')
        self.assertContains(response, 'Brooklyn')
        self.assertContains(response, '10')

    def test_no_events_eventspage(self):
        """Testing the events page on no events in Database"""

        response = self.client.get('/events/')
        self.assertContains(response, 'Sorry, no events right now :('
                                      ' Please come back later.')

    def test_login(self):
        """Test for login"""
        username = 'ayaz'
        password = 'test'
        user = get_user_model()
        user.objects.create_user(username, password=password)
        logged_in = self.client.login(username=username, password=password)
        self.assertTrue(logged_in)
