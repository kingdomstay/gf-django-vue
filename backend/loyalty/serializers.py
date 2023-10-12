from rest_framework import serializers
from .models import Coupon, Loyalty

class LoyaltySerializer(serializers.ModelSerializer):
    class Meta:
        model = Loyalty
        fields = ('points','stars')

class CouponsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = ('descriptions','discount')