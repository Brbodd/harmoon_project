from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    phone_number = models.CharField(
        max_length=11,
        unique=True
    )

class PhoneVerification(models.Model):
    phone_number = models.CharField(
        max_length=11
    )

    code = models.CharField(
        max_length=5
    )

    def __str__(self):
        return self.phone_number