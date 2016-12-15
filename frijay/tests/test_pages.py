from django.test import TestCase, Client
from bs4 import BeautifulSoup
from urllib.request import urlopen

class TestPages(TestCase):

    '''Checks for the title of the navbar is correct'''
    def test_navbar_title(self):
        html = urlopen('https://shabbattable.herokuapp.com/').read()
        soup = BeautifulSoup(html, 'html.parser')
        title = soup.findAll('a',{'class' : 'navbar-brand'})
        self.assertEqual(title[0].get_text(), 'Frijay')

    '''Checks that the right navbar buttons are visible and correct'''
    def test_navbar_buttons(self):
        html = urlopen('https://shabbattable.herokuapp.com/').read()
        soup = BeautifulSoup(html, 'html.parser')
        buttons = soup.findAll('a')
        self.assertEquals(buttons[1].get_text(), ' Join a Dinner')
        self.assertEquals(buttons[2].get_text(), 'About Us')
        self.assertEquals(buttons[3].get_text(), 'How It Works')
        self.assertEquals(buttons[4].get_text(), ' Login')
        self.assertEquals(buttons[5].get_text(), ' Sign Up')

    '''Checks that the title is correct on the homepage'''
    def test_homepageTitle(self):
        html = urlopen('https://shabbattable.herokuapp.com/').read()
        soup = BeautifulSoup(html, 'html.parser')
        self.assertEquals(soup.title.get_text(), 'Frijay')

    '''Checks that the title is correcdt on the events page'''
    def test_eventTitle(self):
        html = urlopen('https://shabbattable.herokuapp.com/events/').read()
        soup = BeautifulSoup(html, 'html.parser')
        self.assertEquals(soup.title.get_text(), 'Events Page')

    '''Checks that the title is correct on the about page'''
    def test_aboutTitle(self):
        html = urlopen('https://shabbattable.herokuapp.com/about/').read()
        soup = BeautifulSoup(html, 'html.parser')
        self.assertEquals(soup.title.get_text(), ' About Us ')

    '''Checks tat the title on the'''
    def test_howWorksTitle(self):
        html = urlopen('https://shabbattable.herokuapp.com/howitworks/').read()
        soup = BeautifulSoup(html, 'html.parser')
        self.assertEquals(soup.title.get_text(), 'How It Works')

    def test_numberOfEvents(self):
        html = urlopen('https://shabbattable.herokuapp.com/events/').read()
        soup = BeautifulSoup(html, 'html.parser')
        events = soup.findAll('div', {'class' : 'thumbnail event'})
        self.assertEquals(len(events), 9)
