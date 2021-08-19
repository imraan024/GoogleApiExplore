from django.contrib.auth import forms
from django.db import models
from django.db.models import fields
from django.forms import ModelForm, widgets
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from .models import UserProfile

class UserForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    username = forms.CharField(max_length=20, required=True)
    password1 = forms.EmailField(max_length=20, required=True)
    password2 = forms.EmailField(max_length=20, required=True)

    widgets = {
            'first_name': forms.TextInput(attrs = {'placeholder' : 'Enter Your First Name'}),
            'last_name': forms.TextInput(attrs = {'placeholder' : 'Enter Your Last Name'}),
            'username': forms.TextInput(attrs = {'placeholder' : 'Email'}),
            'password1': forms.PasswordInput(attrs = {'class': 'password', 'placeholder':'Password'}),
            'password2': forms.PasswordInput(attrs = {'class': 'password', 'placeholder':'Confirm Password'}),
        }

    token = forms.CharField(widget=forms.HiddenInput())
    class Meta:
        model = User
        fields = ('username','first_name','last_name','password1','password2',)

class AuthForm(AuthenticationForm):
    username = forms.EmailField(max_length=50, required=True, widget = forms.TextInput(attrs={'placeholder':'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password', 'class': 'password'}))

    class Meta:
        model = User
        fields = ('username','password',)



class UserProfileForm(forms.ModelForm):
	address = forms.CharField(max_length=100, required=True, widget = forms.HiddenInput())
	town = forms.CharField(max_length=100, required=True, widget = forms.HiddenInput())
	county = forms.CharField(max_length=100, required=True, widget = forms.HiddenInput())
	post_code = forms.CharField(max_length=8, required=True, widget = forms.HiddenInput())
	country = forms.CharField(max_length=40, required=True, widget = forms.HiddenInput())
	longitude = forms.CharField(max_length=50, required=True, widget = forms.HiddenInput())
	latitude = forms.CharField(max_length=50, required=True, widget = forms.HiddenInput())


	class Meta:
		model = UserProfile
		fields = ('address', 'town', 'county', 'post_code', 'country', 'longitude', 'latitude',)

