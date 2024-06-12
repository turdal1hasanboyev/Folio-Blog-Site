from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    profile_photo = models.ImageField(upload_to="ProfilePhotos/", null=True, blank=True)
    biography = models.CharField(max_length=225, null=True, blank=True)
    work = models.CharField(max_length=225, null=True, blank=True)

    def __str__(self):
        return self.username
    