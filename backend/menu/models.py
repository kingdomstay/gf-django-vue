from django.db import models


class Drink(models.Model):
    title = models.CharField(max_length=30, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    price = models.SmallIntegerField(verbose_name="Стоимость")
    photo = models.FileField(verbose_name="Картинка")
    cat = models.ForeignKey("Category", null=True, on_delete=models.PROTECT, verbose_name="Категория")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Напиток"
        verbose_name_plural = "Напитки"
        ordering = ["title", "price", "cat"]


class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name="Категория")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категории позиций"
        verbose_name_plural = "Категории позиций"
        ordering = [
            "id",
            "name",
        ]
