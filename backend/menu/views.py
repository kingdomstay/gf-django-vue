import logging

from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Drink
from .serializers import DrinkSerializer

Logger = logging.getLogger("main")


class DrinkViewSet(viewsets.ModelViewSet):
    queryset = Drink.objects.all()
    serializer_class = DrinkSerializer

    @action(methods=["get"], detail=True)
    def get(self, request, pk=None):
        drink = Drink.objects.get(pk=pk)
        return Response({"drinks": drink.drink})

def login_view(request):
    Logger.info("Получен")
    return HttpResponse("<h1>Hello</h1>")
