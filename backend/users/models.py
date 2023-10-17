from django.conf import settings
from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    telephone = models.CharField(verbose_name="Номер телефона", max_length=15, blank=True, null=True)
    avatar = models.FileField(verbose_name="Фото пользователя", blank=True, null=True)
    points = models.SmallIntegerField(verbose_name="Баллы")
    stars = models.SmallIntegerField(verbose_name="Звездочки")

    def __str__(self):
        return "Profile for user {}".format(self.user.username)

    class Meta:
        verbose_name = "Посетитель"
        verbose_name_plural = "Посетители"
