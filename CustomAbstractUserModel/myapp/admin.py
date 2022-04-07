from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import *
@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ['email','user_name','first_name', 'is_staff', 'is_active']
    list_filter = ['email', 'is_staff', 'is_active']
    fieldsets = (
        (None, {
            'fields': (
                'email','user_name','first_name', 'password','start_date','about'
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
                'email','user_name','first_name','password1','password2','start_date','about','is_staff','is_active'
            )
        }),
    )
    search_fields=('email',)
    ordering=('email',)

