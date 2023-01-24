from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    angel = models.BooleanField()
    founder = models.BooleanField()

    def __str__(self):
        return self.username