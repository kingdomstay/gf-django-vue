import logging

from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Location, News
from .serializers import LocationSerializer, NewsSerializer

Logger = logging.getLogger("main")


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

    @action(methods=["get"], detail=True)
    def get(self, request, pk=None):
        location = Location.objects.get(pk=pk)
        return Response({"location": location.location})


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    @action(methods=["get"], detail=True)
    def get(self, request, pk=None):
        news = News.objects.get(pk=pk)
        return Response({"news": news.news})


def login_view(request):
    Logger.info("Получен")
    return HttpResponse("<h1>Hello</h1>")
