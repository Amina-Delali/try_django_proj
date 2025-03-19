from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.utils.translation import gettext_lazy as _
import uuid

# Create your models here.

# class Account(AbstractUser):
#     id = models.UUIDField(_('id'), primary_key=True, default=uuid.uuid4, editable=False, unique=True)
#     username = models.CharField(_('username'), null=False, blank=False, max_length=50, unique=True)
#     email = models.EmailField(_('email'), null=False, blank=False, unique=True)
#     first_name = models.CharField(_('firstname'), null=False, blank=False, max_length=50)
#     last_name = models.CharField(_('lastname'), null=False, blank=False, max_length=50)
#     is_active = models.BooleanField(_('active'), default=True)
#     is_staff = models.BooleanField(_('staff'), default=False)
#     is_superuser = models.BooleanField(_('superuser'), default=False)
#     date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
#     last_login = models.DateTimeField(_('last login'), auto_now=True)
    