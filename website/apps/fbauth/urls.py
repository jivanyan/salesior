
from django.conf.urls import patterns, include, url
from django.contrib import admin

#from website.views import home, user_login, user_home
#from website.apps.patron.views import  patron_signup, patron_homepage
#from website.apps.venue.views import venue_signup
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'website.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'login/$','fb_login' ),
    url(r'callback/$', 'fb_callback'),	
)
