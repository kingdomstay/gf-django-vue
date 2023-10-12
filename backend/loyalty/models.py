from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Loyalty(models.Model):
    name = models.CharField(max_length=30, verbose_name="Название")
    points = models.SmallIntegerField(verbose_name="Баллы")
    stars = models.SmallIntegerField(verbose_name="Звездочки")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Накопительная система"
        verbose_name_plural = "Накопительная система"
        ordering = ["name", "points", "stars"]


class Coupon(models.Model):
    name = models.CharField(max_length=30, verbose_name="Название")
    descriptions = models.TextField(verbose_name="Описание")
    discount = models.SmallIntegerField(
        validators=[MaxValueValidator(100), MinValueValidator(1)],
        verbose_name="Размер скидки",
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Скидки и акции"
        verbose_name_plural = "Скидки и акции"
        ordering = ["name", "discount"]
