from django.shortcuts import render
from rest_framework import generics
from .models import Drink
from .serializers import DrinkSerializer

# Create your views here.
class DrinkAPIView(generics.ListAPIView):
    queryset = Drink.objects.all()
    serializer_class = DrinkSerializer