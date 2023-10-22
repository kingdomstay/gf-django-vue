from django.contrib import admin

from .models import *


class LocationAdmin(admin.ModelAdmin):
    list_display = ("name", "address")
    list_display_links = ("name",)
    search_fields = ("name", "address")
    list_editable = ("address",)


class NewsAdmin(admin.ModelAdmin):
    list_display = ("title", "description")
    list_display_links = ("title", "description")
    search_fields = ("title",)


admin.site.register(Location, LocationAdmin)
admin.site.register(News, NewsAdmin)
