from django.conf.urls import patterns, include, url
from django.contrib import admin
from website.views import home, user_login, user_home
from website.apps.patron.views import  patron_signup, patron_homepage
from website.apps.venue.views import venue_signup
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'website.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', home),
    url(r'^home/', home),
    url(r'^homepage',user_home, name = "homepage"),	
    #url(r'^facebook/', include('fbauth.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^signup/patron/', patron_signup, name = "Patron Registration"),
    url(r'^signup/venue/', venue_signup, name = "Venue Registration"), 		
    url(r'^login/$', user_login, name='login'),	
    url(r'^facebook/', include('django_facebook.urls')),
    url(r'^accounts/', include('django_facebook.auth_urls'))	
)
