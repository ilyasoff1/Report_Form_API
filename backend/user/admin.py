from django.contrib import admin
from .models import Profile
from django.contrib.auth.admin import UserAdmin

@admin.register(Profile)
class ProfileAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Custom Fields', {
            'fields': ('contact', 'department')
        }),
    )
