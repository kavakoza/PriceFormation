from django.contrib.auth.models import AbstractUser
from django.db import models
from constants import NULLABLE


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Email')
    phone_number = models.CharField(max_length=35, verbose_name='Phone Number', **NULLABLE)
    city = models.CharField(max_length=200, verbose_name='City', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
