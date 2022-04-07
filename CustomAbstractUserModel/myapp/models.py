
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from .managers import CustomUser
# Create your models here.

#permissionmixin le django ko default permisssion use garxa with custom UserModel
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("Email Address"), max_length=254, unique=True)
    user_name = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=50)
    start_date = models.DateTimeField(default=timezone.now)
    about = models.TextField(_('About'), max_length=200, blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    objects = CustomUser()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name','first_name']

    def __str__(self):
        return self.user_name
