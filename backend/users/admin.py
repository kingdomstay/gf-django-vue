from django.contrib import admin
from .models import *


# class VisitorAdmin(admin.ModelAdmin):
#     list_display = ("name")


# #     list_display_links = ("firstName", "surName")
# #     search_fields = ("firstName", "surName")
# #     list_editable = ("email", "telephone")


# admin.site.register(Visitor, VisitorAdmin)


@admin.register(Visitor)
class VisitorAdmin(admin.ModelAdmin):
    list_display = ("name", "email")
