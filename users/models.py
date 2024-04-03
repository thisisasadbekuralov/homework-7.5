from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    email = models.EmailField()
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username



