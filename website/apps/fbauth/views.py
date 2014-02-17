# Create your views here.
import cgi
import json
import urllib
from django.conf import settings
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

from .models import FacebookProfile



def add_user(username, password, email):
        user = User.objects.create_user(
            username=username,
            password=password,
            email=email
        )
        user.is_active = True
        user.save()
        return user



def create_fb_profile(id, fb_id, access_token):
	FacebookProfile.objects.create(
        	user_id=id,
                facebook_id=fb_id,
                access_token=access_token
        )

def get_profile(request, token = None):
	args = {
		'client_id':settings.FACEBOOK_APP_ID,
		'client_secret': settings.FACEBOOK_APP_SECRET,
		'redirect_uri': '/homepage/' ,
		'code':token,
	}    
	target = urllib.urlopen('https://graph.facebook.com/oauth/access_token?'+ urllib.urlencode(args)).read()
	response = cgi.parse_qs(target)
	access_token = response['access_token'][-1]
	return access_token


def fb_login(request):
	args = {
		'client_id': settings.FACEBOOK_APP_ID,
		'scope': settings.FACEBOOK_SCOPE,
		'redirect_uri': request.build_absolute_uri(reverse('fb_callback')),
	}
	return HttpResponseRedirect('https://graph.facebook.com/oauth?'+urllib.urlencode(args)) 

def fb_callback(request):
	access_token = get_profile(request,request.GET.get('code'))
	fb_profile = urllib.urlopen('https://graph.facebook.com/me?access_token={0}'.format(access_token))	
	fb_profile = json.load(fb_profile)
	try:
		fb_user = FacebookProfile.objects.get(facebook_id = fb_profile['id'])
		fb_user.access_token = access_token
		fb_user.save()
		user = User.objects.get(pk = fb_user.user_id)
		user.backend = 'django.contrib.auth.backends.ModelBackend'
		if user.is_active:
			auth_login(request, user)
			return HttpResponseRedirect(reverse('homepage'))
		else:
			return HttpResponseRedirect(reverse('login'))
	except FacebookProfile.DoesNotExist:
		fb_username = fb_profile.get('username',fb_profile['email'].split('@')[0])
		fb_id = fb_profile.id
		fb_email = fb_profile.email
		user = add_user(fb_username, fb_username, fb_email)
		create_fb_profile(user.id, fb_id, access_token)
		user = authenticate(username = fb_username, password = fb_username)
		auth_login(request, user)
		return HttpResponseRedirect(reverse('homepage'))
		
	

	
