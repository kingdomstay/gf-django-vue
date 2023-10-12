from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Drink
from .serializers import DrinkSerializer

# Create your views here.
class DrinkAPIView(APIView):
    def get(self, request):
        lst = Drink.objects.all().values()
        return Response({'drinks': list(lst)})
    queryset = Drink.objects.all()
    serializer_class = DrinkSerializer