from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=30, verbose_name="Название кафе")
    address = models.TextField(verbose_name="Адрес кафе")
    photo = models.FileField(verbose_name="Фотография")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Местоположение"
        verbose_name_plural = "Местоположение"
        ordering = ["name", "address"]
