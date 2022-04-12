from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from .managers import AccountManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """
    Кастомизированная модель пользователя.
    Поля: email, username, is_staff, is_active.
    """
    email = models.EmailField(max_length=155, unique=True)
    username = models.CharField(max_length=100, unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = AccountManager()

    def __str__(self):
        return self.username