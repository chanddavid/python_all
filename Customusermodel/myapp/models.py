from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from .manager import UserManager

# Create your models here.

class User(AbstractUser):
    username=None
    email=models.EmailField(_('Email address'),unique=True)
    bio=models.TextField(max_length=200,null=True,blank=True)
    last_logout_time=models.DateTimeField(null=True,blank=True)

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
    