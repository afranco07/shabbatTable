from django.test import TestCase
from django.contrib.auth.models import User
from django.test import Client

class ViewsTest(TestCase):

    def setUp(self):
        user = User.objects.create_user('bob', '', 'temp')
        user.set_password('temp')
        self.client.login(username='bob', password='temp')
        self.assertTrue(user.is_authenticated())

    def test_login(self):
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
        user = User.objects.create_user('bob', '', 'temp')
        user.set_password('temp')
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
        user = User.objects.create_user('bob', '', 'temp')
        user.set_password('temp')
        self.client.login(username='bob', password='temp')
        response = self.client.get("/host/")
        self.assertEqual(response.status_code, 200)

    '''Test the myevents.html'''
    def test_reservations(self):
        user = User.objects.create_user('bob', '', 'temp')
        user.set_password('temp')
        self.client.login(username='bob', password='temp')
        response = self.client.get("/myevents/")
        self.assertEqual(response.status_code, 200)