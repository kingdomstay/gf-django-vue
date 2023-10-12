from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Loyalty(models.Model):
    name = models.CharField(max_length=30)
    points = models.SmallIntegerField()
    stars = models.SmallIntegerField()
    def __str__(self):
        return self.name

class Coupon(models.Model):
    name = models.CharField(max_length=30)
    descriptions = models.TextField()
    discount = models.SmallIntegerField(
        validators=[
            MaxValueValidator(100),
            MinValueValidator(1)]
    )
    def __str__(self):
        return self.name
