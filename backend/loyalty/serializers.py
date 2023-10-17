from rest_framework import serializers
from .models import Coupon, Loyalty


class LoyaltySerializer(serializers.ModelSerializer):
    class Meta:
        model = Loyalty
        fields = "__all__"


class CouponsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = "__all__"
