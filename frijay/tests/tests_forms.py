    
from datetime import datetime, timedelta
from django import forms
from django.contrib.auth.models import User
from django.test import TestCase
from frijay.forms import UserForm


class FormsTest(TestCase):

	def test_valid_data(self):

	    form = UserForm({
	        'first_name': "Avi",
	        'last_name': "Kirschenbaum",
	        'username': "Avi123",
	        'email': "avikirschenbaum@gmail.com",
	        'password': "ABC123",
		})
	    self.assertTrue(form.is_valid())
	    check = form.save()
	    self.assertEqual(check.first_name, "Avi")
	    self.assertEqual(check.last_name, "Kirschenbaum")
	    self.assertEqual(check.username, "Avi123")
	    self.assertEqual(check.email, "avikirschenbaum@gmail.com")
	    self.assertEqual(check.password, "ABC123")