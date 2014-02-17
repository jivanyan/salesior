import os

#settings.configure()

def populate_patrons():
	add_user("x", "test")

def add_user(name, pwd):
	u = User.objects.get_or_create(username = name, password = pwd)
	return u
def add_five_more_patrons():
	#p = Patron.objects.filter



if __name__ == '__main__':
	print "Starting commerce population script..."
	os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'website.settings')
	from django.contrib.auth.models import User
	from .website.apps.patron.models import *
	from .website.apps.venue.models import *
	populate_patrons()
	#populate_venues()

	print "FINISH"
