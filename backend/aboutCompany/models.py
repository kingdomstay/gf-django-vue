from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=30)
    address = models.TextField()
    photo = models.FileField()
    def __str__(self):
            return self.name