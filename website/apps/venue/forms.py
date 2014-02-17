from venue.models import *
from django.contrib.auth.models import User
from django import forms

class VenueForm(forms.ModelForm):
	name = forms.CharField(max_length = 128, help_text = "Enter the name")
	class Meta:
		model = Venue
		exclude = ['str_id', 'hash_id','date_created','lat','lng','user']
