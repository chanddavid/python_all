from dataclasses import field
from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django.contrib.auth.models import User
from importlib_metadata import MetadataPathFinder
from .models import Order
from django.utils.translation import gettext, gettext_lazy as _
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer','product','status','review']
        labels = {
            'customer': 'Customer',
            'product': 'Product',
            'status': 'Status',
        }

class RegisterForm(UserCreationForm):
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(
        render_value=True, attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(
        render_value=True, attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control '}),
            'last_name': forms.TextInput(attrs={'class': 'form-control '}),
            'email': forms.EmailInput(attrs={'class': 'form-control '}),
        }

class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'autofocus': True}))
    password = forms.CharField(label=_("Password"), strip=False, widget=forms.PasswordInput(
        render_value=True, attrs={'class': 'form-control', 'autocomplete': 'current-password'}))
