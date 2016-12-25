'''These are tests that checks all of the content that is loaded onto the pages'''
from urllib.request import urlopen
from django.test import TestCase
from bs4 import BeautifulSoup

class TestPages(TestCase):
    '''These are tests that checks all of the content that is loaded onto the pages'''

    def test_navbar_title(self):
        """Checks for the title of the navbar is correct"""
        html = urlopen('https://shabbattable.herokuapp.com/').read()
        soup = BeautifulSoup(html, 'html.parser')
        title = soup.findAll('a', {'class' : 'navbar-brand'})
        self.assertEqual(title[0].get_text(), 'Frijay')

    def test_navbar_buttons(self):
        """Checks that the right navbar buttons are visible and correct"""
        html = urlopen('https://shabbattable.herokuapp.com/').read()
        soup = BeautifulSoup(html, 'html.parser')
        buttons = soup.findAll('a')
        self.assertEqual(buttons[1].get_text(), ' Join a Dinner')
        self.assertEqual(buttons[2].get_text(), 'About Us')
        self.assertEqual(buttons[3].get_text(), 'How It Works')
        self.assertEqual(buttons[4].get_text(), ' Login')
        self.assertEqual(buttons[5].get_text(), ' Sign Up')

    def test_homepage_title(self):
        """Checks that the title is correct on the homepage"""
        html = urlopen('https://shabbattable.herokuapp.com/').read()
        soup = BeautifulSoup(html, 'html.parser')
        self.assertEqual(soup.title.get_text(), 'Frijay')

    def test_event_title(self):
        """Checks that the title is correcdt on the events page"""
        html = urlopen('https://shabbattable.herokuapp.com/events/').read()
        soup = BeautifulSoup(html, 'html.parser')
        self.assertEqual(soup.title.get_text(), 'Events Page')

    def test_about_title(self):
        """Checks that the title is correct on the about page"""
        html = urlopen('https://shabbattable.herokuapp.com/about/').read()
        soup = BeautifulSoup(html, 'html.parser')
        self.assertEqual(soup.title.get_text(), ' About Us ')

    def test_how_works_title(self):
        """Checks the title on the how it works page"""
        html = urlopen('https://shabbattable.herokuapp.com/howitworks/').read()
        soup = BeautifulSoup(html, 'html.parser')
        self.assertEqual(soup.title.get_text(), 'How It Works')

    def test_number_of_events(self):
        """Checks that the events page has the correct number of events from db"""
        html = urlopen('https://shabbattable.herokuapp.com/events/').read()
        soup = BeautifulSoup(html, 'html.parser')
        events = soup.findAll('div', {'class' : 'thumbnail event'})
        self.assertEqual(len(events), 9)
