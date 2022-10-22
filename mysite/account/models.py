from django.db import models
from django.contrib.auth.models import AbstractUser


# USER MODEL EXTENSION
class CustomUser(AbstractUser):
    # DATABASE FIELDS
    avatar = models.ImageField(upload_to="users/avatars", null=True, blank=True, verbose_name="Avatar")
