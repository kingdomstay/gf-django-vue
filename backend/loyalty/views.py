from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Coupon, Loyalty
from .serializers import CouponsSerializer,LoyaltySerializer

# Create your views here.
class LoyaltyAPIView(APIView):
    def get(self, request):
        lst = Loyalty.objects.all().values()
        return Response({'loyalty': list(lst)})
    queryset = Loyalty.objects.all()
    serializer_class = LoyaltySerializer

class CouponsAPIView(APIView):
    def get(self, request):
        lst = Coupon.objects.all().values()
        return Response({'coupons': list(lst)})
    queryset = Coupon.objects.all()
    serializer_class = CouponsSerializer