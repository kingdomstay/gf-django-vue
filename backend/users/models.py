from django.db import models


# Create your models here.
class Visitor(models.Model):
    # firstName = models.CharField(verbose_name="Имя", max_length=255)
    # surName = models.CharField(verbose_name="Фамилия", max_length=255)
    # email = models.EmailField(
    #     max_length=255, verbose_name="Электронный адрес посетителя"
    # )
    # telephone = models.CharField(verbose_name="Номер телефона", max_length=15)
    # avatar = models.FileField(verbose_name="Фото пользователя", blank=True, null=True)
    name = models.CharField(verbose_name="Имя посетителя", max_length=255)
    email = models.EmailField(
        max_length=255, verbose_name="Электронный адрес посетителя"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Посетитель"
        verbose_name_plural = "Посетители"
