from django.contrib.auth.models import AbstractUser
from django.db import models

from mainapp.models import NULLABLE


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='почта')
    phone = models.CharField(max_length=30, verbose_name='телефон', **NULLABLE)
    country = models.CharField(max_length=100, verbose_name='страна', **NULLABLE )
    avatar = models.ImageField(upload_to='usersapp/', verbose_name='аватар', **NULLABLE)
    email_verify = models.IntegerField(verbose_name='код верификации email', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

