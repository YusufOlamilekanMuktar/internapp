from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.db import models

class CreateUSerForm(UserCreationForm):
	"""docstring for CreateUSerForm"""
	username	=	forms.CharField(
						widget = forms.TextInput(attrs	=	{
										"placeholder"	:'Username',
										"id"			: 'UserName',
										"value"			: '',}))
	email		=	forms.CharField(
						widget = forms.EmailInput(attrs	=	{"placeholder"	:'Email',}))
	password1	=	forms.CharField(
						widget = forms.PasswordInput(attrs	=	{
										"placeholder"	:'Password',
										"id"			: 'myInput',}))
	password2	=	forms.CharField(
						widget = forms.PasswordInput(attrs	=	{
										"placeholder"	:'Password Confirmation',
										"id"			: 'myInput',}))
	class Meta:
		model 	=	User
		fields	=	['username', 
					'email', 
					'password1',
					 'password2'
		]