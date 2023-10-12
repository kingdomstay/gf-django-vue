from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Location
from .serializers import LocationSerializer

# Create your views here.
class LocationAPIView(APIView):
    def get(self, request):
        lst = Location.objects.all().values()
        return Response({'location': list(lst)})
    queryset = Location.objects.all()
    serializer_class = LocationSerializer