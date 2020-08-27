from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
	path('', views.home, name='Home'),
    path('register/', views.registerPage, name='Register'),
    path('login/', views.loginPage, name='Login'),
    path('logout/', views.logoutUser, name='Logout'),
    path('profile/', views.profilePage, name='Profile'),
    path('user/', views.userPage, name='Userpage'),
    path('send_email/', views.sendEmail, name='sendEmail'),
]
