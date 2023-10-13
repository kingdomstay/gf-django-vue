from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import VisitorSerializer
from .models import Visitor
from rest_framework.decorators import action
from rest_framework import viewsets
import logging
from django.http.response import HttpResponse

Logger = logging.getLogger("main")


class VisitorViewSet(viewsets.ModelViewSet):
    queryset = Visitor.objects.all()
    serializer_class = VisitorSerializer


def login_view(request):
    Logger.info("Получен")
    return HttpResponse("<h1>Hello</h1>")
