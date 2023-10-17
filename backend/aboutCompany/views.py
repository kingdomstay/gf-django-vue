from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Location
from .serializers import LocationSerializer
from rest_framework.decorators import action
from rest_framework import viewsets
import logging
from django.http.response import HttpResponse

Logger = logging.getLogger("main")


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

    @action(methods=["get"], detail=True)
    def get(self, request, pk=None):
        location = Location.objects.get(pk=pk)
        return Response({"location": location.location})


def login_view(request):
    Logger.info("Получен")
    return HttpResponse("<h1>Hello</h1>")
