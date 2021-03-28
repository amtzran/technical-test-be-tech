from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField('email address', unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    name = models.CharField(max_length=255)
    phone = models.CharField(null=False, max_length=11)
    gender = models.CharField(max_length=255)
    photo = models.ImageField(null=True, upload_to='users')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
