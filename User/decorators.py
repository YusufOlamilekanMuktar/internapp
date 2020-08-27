from django.http import HttpResponse
from django.shortcuts import redirect


def unauthenticated_user(view_func):
	def wrap_func(request, *args, **kwargs):
		if request.user.is_authenticated:
			return redirect('Profile')
		else:
			return view_func(request, *args, **kwargs)
	return wrap_func
def users_allowed(allowed_roles=[]):
	def decorator(view_func):
		def wrap_func(request, *args, **kwargs):
			group = None
			if request.user.groups.exists():
				group = request.user.groups.all()[0].name
			
			if group in allowed_roles:
				return view_func(request, *args, **kwargs)
			else:
				return HttpResponse('You are not allowed to view this page')
		return wrap_func
	return decorator
def admin_only(view_func):
	def wrap_func(request, *args, **kwargs):
		group = None
		if request.user.groups.exists():
			group = request.user.groups.all()[0].name
		
		if group == 'users':
			return redirect('Userpage')
		
		if group == 'admin':
			return view_func(request, *args, **kwargs)
	return wrap_func