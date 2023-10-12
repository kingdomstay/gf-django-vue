from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Loyalty(models.Model):
    points = models.IntegerField
    stars = models.IntegerField

class Coupons(models.Model):
    descriptions = models.TextField
    discount = models.IntegerField(
        validators=[
            MaxValueValidator(100),
            MinValueValidator(1)]
    )
