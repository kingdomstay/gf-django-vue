from django.contrib import admin

from .models import *


class CouponAdmin(admin.ModelAdmin):
    list_display = ("name", "descriptions", "discount")
    list_display_links = ("name",)
    search_fields = ("name",)
    list_editable = ("descriptions", "discount")


admin.site.register(Coupon, CouponAdmin)
