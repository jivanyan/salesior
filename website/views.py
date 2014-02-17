from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib import auth
#from fbauth.facebook import get_user_info_after_auth
from django_facebook.utils import get_registration_backend, get_instance_for
from django_facebook.decorators import facebook_required_lazy
from django.contrib.auth import authenticate, login

from django.core.mail import send_mail

def home(request):
        context = RequestContext(request)

        #if not request.user.is_authenticated():
        #:        return HttpResponse("Unauthenticated user")

        return render_to_response(
                'homepage.html',
                {'username': request.user.username }, context)
	

@facebook_required_lazy
def user_home(request, graph):
	context = RequestContext(request)
	backend = get_registration_backend()
	converter = get_instance_for('user_conversion', graph)
	if not graph:
		raise ValueError('No graph')
	else:
		x = graph.get('me/friends')
		f = x['data']
		#return HttpResponse("Friends %s" % f)
		#graph.set('me/feed', message = 'Salesior is coming soon..', url = 'http://www.facebook.com')	
		#send_mail('Successfull login in salesior', 'Congrats..', 'lyukar@gmail.com', ['ajivanyan@aua.am'], fail_silently = False)
		return render_to_response(
			'patron/patron_homepage.html',	
			{'friendlist':f}, context)


def user_login(request):
	context = RequestContext(request)
	if request.method == 'POST':
		username = request.POST['username']
	        password = request.POST['password']
 		user = authenticate(username=username, password=password)

       		if user is not None:
                      	if user.is_active:
                          	login(request, user)
                		return HttpResponseRedirect('/home/')
            		else:
                		return HttpResponse("Your Salesior account is disabled.")
        	else:
              		print "Invalid login details: {0}, {1}".format(username, password)
            		return HttpResponse("Invalid login details supplied.")

       	else:
                return render_to_response('login.html', {}, context)
