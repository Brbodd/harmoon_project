from django.db import models
from account_module.models import User

class Reservation(models.Model):

    user = models.ForeignKey(
        User, on_delete=models.CASCADE
    )

    date = models.DateField()

    time = models.TimeField()

    def __str__(self):
        return f"{self.date} - {self.time}"