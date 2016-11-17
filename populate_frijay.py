import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shabbattable.settings')

import django
django.setup()
from frijay.models import User, Event

def populate():
	"""First, we will create lists of dictionaries containing the 
	pages we want to add into each category.
	Then we will create a dictionary of dictionaries for our categories.
	This might seem a little bit confusing, but it allows us to iterate	
	through each data structure, and add the data to our models.
	"""
	users = [
		{"first_name": "Jake",
		 "last_name":"Buchbauer",
		 "email":"bjake@gmail.com",
		 "password":"4u32urjweht93"},
		{"first_name": "Melissa",
		 "last_name":"Kirsch",
		 "email":"m342@gmail.com",
		 "password":"4*@r38HF*(SHg"},
		{"first_name": "Keli",
		 "last_name":"Heurer",
		 "email":"sparkles95@yahoo.com",
		 "password":"mlpfms92n"} ]

	events = [{"title":"Friday Dinner with the Kirschenbaums"},
			  {"title":"The Kirkoffs"}]

	""" If you want to add more categories or pages, add themm
	to the dictionary above.

	The code below goes through the cats dictionary, then adds each 
	category, and then adds all the associated pages for that category.

	"""

	for u in users:
		add_user(u["first_name"], u["last_name"], u["email"], u["password"])	
	
	for e in events:
		add_event(e["title"])


def add_user(firstname,lastname,email,password):
	u = User.objects.get_or_create(first_name=firstname, last_name=lastname,email=email, password=password)[0]
	u.save()
	return u

def add_event(title):
	c = Event.objects.get_or_create(title=title)[0]
	c.save()
	return c

# Start execution here!
if __name__ == '__main__':
	print("Starting Frijay population script...")
	populate()















