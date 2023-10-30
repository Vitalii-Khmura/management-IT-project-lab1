from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class People(models.Model):
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.IntegerField(blank=True)
