from patron.models import  *
from django.contrib.auth.models import User
from django import forms

class UserForm(forms.ModelForm):
	username = forms.CharField(help_text = '')
        password = forms.CharField(widget = forms.PasswordInput())
        confirm_password = forms.CharField(widget = forms.PasswordInput())
        class Meta:
                model = User
                fields = ('username', 'email','password',)

class PatronForm(forms.ModelForm):
	class Meta:
		model = Patron
		exclude = ['user','all_venues']
