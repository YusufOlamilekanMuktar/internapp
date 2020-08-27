from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
# Register your models here.

admin.site.unregister(User)

@admin.register(User)
class CustomerUserAdmin(UserAdmin):
	list_filter	=	[
		'date_joined',
		'groups',
		'is_superuser',
		'is_staff',
		'is_active'
		]
	readonly_fields	=	[
		'date_joined',
	]

	actions = [
        'activate_users',
        'deactivate_users',
        'staff_users',
        'un_staff_users',
    ]

	def activate_users(self, request, queryset):
	    cnt = queryset.filter(is_active=False).update(is_active=True)
	    self.message_user(request, 'Activated {} users.'.format(cnt))
	activate_users.short_description = 'Activate Users'

	def deactivate_users(self, request, queryset):
		cnt = queryset.filter(is_active=True).update(is_active=False)
		self.message_user(request, 'Deactivated {} users.'.format(cnt))
	deactivate_users.short_description = 'Deactivate Users'

	def staff_users(self, request, queryset):
		cnt = queryset.filter(is_staff=False).update(is_staff=True)
		self.message_user(request, 'Staffed {} users.'.format(cnt))
	staff_users.short_description = 'Staff Users'
	def un_staff_users(self, request, queryset):

		cnt = queryset.filter(is_staff=True).update(is_staff=False)
		self.message_user(request, 'Un-staffed {} users.'.format(cnt))
	un_staff_users.short_description = 'Un-staff Users'