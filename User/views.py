from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group, Permission
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CreateUSerForm
from .decorators import unauthenticated_user, users_allowed, admin_only
from django.core.mail import send_mail
from django.http import HttpResponse
# Create your views here.

def home(request):
	context	=	{}
	return render(request, 'home.html', context)

@unauthenticated_user
def registerPage(request):	
	form 				=	CreateUSerForm()
	if request.method 	== 'POST':
		form 			=	CreateUSerForm(request.POST)
		if form.is_valid():
			user = form.save()
			#form 		=	CreateUSerForm()
			username 		=	form.cleaned_data.get('username')
			group 		=	Group.objects.get(name='users')
			user.groups.add(group)

			messages.success(request, 'Account successfully created for ' +  username)
			return redirect('Login')
	context				=	{
							'form': form
			}
	return render(request, 'register.html', context)

@unauthenticated_user
def loginPage(request):
	if request.method 	== 'POST':
		username		=	request.POST.get('username')
		password		=	request.POST.get('password')

		user 			=	authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('Profile')
		else:
			messages.info(request, 'Username or Password is incorrect, Try again')
	context	=	{}
	return render(request, 'login.html', context)
def logoutUser(request):
	logout(request)
	return redirect('Login')

@login_required(login_url = 'Login')
@admin_only
def profilePage(request):
	usernames = User.objects.filter(groups__name='users')
	return render( request, 'profile.html', {'usernames':usernames})

@login_required(login_url = 'Login')
# @admin_only
def userPage(request):
	context		=	{}
	return render(request, 'profile_user.html', context)

@login_required(login_url = 'Login')
@admin_only
def sendEmail(request):
    if request.method == 'POST':
        email = request.POST.get("email")
        send_mail('Application for Internship', 'Internship Application', 'no-reply@internapp.com', [email], fail_silently=False)
        # return HttpResponse("Mail successfully sent to " + email)
        messages.success(request, 'Email successfully sent to ' + email)
    return render(request, 'send_email.html')