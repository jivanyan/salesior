from django.contrib import admin
from patron.models import *
from django_facebook.models import FacebookCustomUser
admin.site.register(Patron)
admin.site.register(Friendship)
admin.site.register(VenueRelationship)
admin.site.register(FacebookCustomUser)
