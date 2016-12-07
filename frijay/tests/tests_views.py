from django.test import TestCase
from django.contrib.auth import get_user_model
from frijay.models import Event

class ViewsTest(TestCase):

    '''Test the index.html page'''
    def test_indexPage(self):
        """Tests the landing page"""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    # '''Test the reservation.html page'''
    # def test_reservationPage(self):
    #     """Tests the reservations page """
    #     response = self.client.get("/reservations/")
    #     self.assertEqual(response.status_code, 200)

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
        response = self.client.get("/login")
        self.assertEqual(response.status_code, 200)

    '''Test the signup.html'''
    def test_signUpPage(self):
        """Tests the signup page"""
        response = self.client.get("/signup/")
        self.assertEqual(response.status_code, 200)


    """Test whether our events show up on the homepage"""

    def setUp(self):
        self.user = get_user_model().objects.create(username='some_user')

    def test_one_event(self):
        Event.objects.create(title='Shabbat',address='testaddress',city='Brooklyn',state='New York',
                             phone='1231231234',date='2016-12-07',time1='03:24:12',time2="03:24:12",
                             openSeats='10',additionalDetails='None')
        response = self.client.get('/')
        self.assertContains(response, 'Shabbat')
        self.assertContains(response, 'Brooklyn')
        self.assertContains(response, '10')

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
