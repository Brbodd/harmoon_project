from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    phone_number = models.CharField(max_length=200)

class Reservation(models.Model):

    user = models.ForeignKey(
        User, on_delete=models.CASCADE
    )

    date = models.DateField()

    time = models.TimeField()

    def __str__(self):
        return f"{self.date} - {self.time}"