from django.db import models

class Location(models.Model):
    address = models.TextField
    photo = models.FileField
