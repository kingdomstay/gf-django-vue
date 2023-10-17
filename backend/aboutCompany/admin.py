from django.contrib import admin
from .models import *


class LocationAdmin(admin.ModelAdmin):
    list_display = ("name", "address")
    list_display_links = ("name",)
    search_fields = ("name", "address")
    list_editable = ("address",)


admin.site.register(Location, LocationAdmin)
