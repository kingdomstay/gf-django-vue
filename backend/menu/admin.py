from django.contrib import admin
from .models import *


class DrinkAdmin(admin.ModelAdmin):
    list_display = ("title", "price", "cat")
    list_display_links = ("title",)
    search_fields = ("title", "price", "cat")
    list_editable = ("price", "cat")
    list_filter = ("cat",)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
    )
    list_display_links = ("name",)
    search_fields = ("name",)


admin.site.register(Drink, DrinkAdmin)
admin.site.register(Category, CategoryAdmin)
