from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Time_sheet(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    description = models.CharField(max_length=300, blank=True)
    fk_user = models.ForeignKey(
        User, related_name="user_registro", on_delete=models.PROTECT
    )


class Vacations(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    confirmed = models.BooleanField(default=True)
    fk_user = models.ForeignKey(
        User, related_name="user_ferias", on_delete=models.PROTECT
    )


class Holidays(models.Model):
    description = models.CharField(max_length=300)
    day = models.CharField(max_length=2)
    month = models.CharField(max_length=2)
    year = models.CharField(max_length=4)

class NewUser(models.Model):
    pass