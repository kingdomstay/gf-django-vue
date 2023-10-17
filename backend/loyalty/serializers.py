from rest_framework import serializers
from .models import Coupon, Loyalty


class CouponsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = "__all__"
