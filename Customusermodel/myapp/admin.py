import imp
from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin 
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.
from .models import *


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ['email', 'is_staff', 'is_active']
    list_filter = ['email', 'is_staff', 'is_active']
    fieldsets = (
        (None, {
            'fields': (
                'email', 'password','bio','last_logout_time'
            ),
        }),
        ('permissions',{   
             "fields": (
                'is_staff', 'is_active'
            ),
        })
    )
    add_fieldsets=(
        (None, {
            'classes': (
                'wide',
            ),
            'fields':(
                'email','password1','password2','bio','last_logout_time','is_staff','is_active'
            )
        }),
    )
    search_fields=('email',)
    ordering=('email',)
