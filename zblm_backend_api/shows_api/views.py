from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import ShowSerializer
from .models import Show

class ShowList(generics.ListCreateAPIView):
    queryset = Show.objects.all().order_by('id') 
    # tell django how to retrieve all objects from the DB, order by id ascending
    serializer_class = ShowSerializer 
    # tell django what serializer to use

class ShowDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Show.objects.all().order_by('id')
    serializer_class = ShowSerializer