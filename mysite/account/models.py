from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.urls import reverse


# USER MODEL EXTENSION
class CustomUser(AbstractUser):
    # DATABASE FIELDS
    avatar = models.ImageField(upload_to="users/avatars", null=True, blank=True, verbose_name="Avatar")
    # MANAGER TO CREATE USERS
    objects = UserManager()

    # META CLASS
    class Meta:
        ordering = ['username']

    # TO STRING METHOD
    def __str__(self):
        return self.username

    # ABSOLUTE URL METHOD
    def get_absolute_url(self):
        return reverse('profile', kwargs={'id': self.pk})
