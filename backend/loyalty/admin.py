from django.contrib import admin

from .models import *


class LoyaltyAdmin(admin.ModelAdmin):
    list_display = ("name", "points", "stars")
    list_display_links = ("name",)
    search_fields = ("name", "points", "stars")
    list_editable = ("points", "stars")


class CouponAdmin(admin.ModelAdmin):
    list_display = ("name", "descriptions", "discount")
    list_display_links = ("name",)
    search_fields = ("name",)
    list_editable = ("descriptions", "discount")


admin.site.register(Loyalty, LoyaltyAdmin)
admin.site.register(Coupon, CouponAdmin)
