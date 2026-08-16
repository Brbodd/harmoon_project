from django.db import models
from django.contrib.auth.models import User


class Reservation(models.Model):

    user = models.ForeignKey(
        User, on_delete=models.CASCADE
    )

    date = models.DateField()

    time = models.TimeField()

    def __str__(self):
        return f"{self.user} - {self.date} - {self.time}"