from django.db import models

class Drink(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    price = models.SmallIntegerField()
    photo = models.FileField()
    cat = models.ForeignKey('Category', null=True, on_delete=models.PROTECT)

    def __str__(self):
        return self.title
    
class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

