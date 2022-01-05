from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    city = models.CharField(max_length=50, blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    card_number = models.CharField(max_length=15, blank=True, null=True)
