from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from venue.forms import *
from patron.forms import UserForm
from django.contrib.auth import authenticate, login as auth_login
 

def venue_signup(request):
        context = RequestContext(request)
        registered = False
        if request.method == 'POST':
                user_form = UserForm(data = request.POST)
                venue_form = VenueForm(data = request.POST)
                if user_form.is_valid() and venue_form.is_valid():
                        user = user_form.save()
                        user.set_password(user.password)
                        #user.set_username(user.email)
                        user.save()
                        venue = venue_form.save(commit = False)
                        venue.user = user
                        venue.save()
                        registered = True
		else:
			print user_form.errors, venue_form.errors
	else:
		user_form = UserForm()
		venue_form = VenueForm()
	return render_to_response(
		'venue/venue_signup.html',
		{'user_form':user_form, 'profile_form':venue_form,'registered':registered},
		context)
                                                              
