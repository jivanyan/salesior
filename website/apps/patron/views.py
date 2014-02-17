from django.shortcuts import render

from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from patron.forms import *
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required


@login_required
def patron_homepage(request):
	return render_to_response('patron/homepage.html',{},context)

def patron_signup(request):
        context = RequestContext(request)
        registered = False
        if request.method == 'POST':
                user_form = UserForm(data = request.POST)
                profile_form = PatronForm(data = request.POST)
                if user_form.is_valid() and profile_form.is_valid():
                        user = user_form.save()
                        user.set_password(user.password)
                        #user.set_username(user.email)
                        user.save()
                        profile = profile_form.save(commit = False)
                        profile.user = user
                        #if 'picture' in request.FILES:
                        #        profile.picture = request.FILES['picture']
                        profile.save()
                        registered = True
                else:
                        print user_form.errors, profile_form.errors
        else:
                user_form = UserForm()
                profile_form = PatronForm()
        return render_to_response(
                'patron/patron_signup.html',
                {'user_form':user_form, 'profile_form':profile_form, 'registered':registered}, context)




