# models.py
from django.db import models

class UserDetails(models.Model):
    name = models.CharField(max_length=255)
    contact = models.PositiveIntegerField()
    email = models.EmailField()
