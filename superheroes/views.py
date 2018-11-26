from django.shortcuts import render
from .models import Publisher,SuperHeroe
from .serializers import PublisherSerializer,SuperHeroeSerializer
from rest_framework import generics
# Create your views here.
class SuperHeroeList(generics.ListCreateAPIView):
    queryset= SuperHeroe.objects.all()
    serializer_class= SuperHeroeSerializer

class SuperHeroeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset= SuperHeroe.objects.all()
    serializer_class= SuperHeroeSerializer

class PublisherList(generics.ListCreateAPIView):
    queryset= Publisher.objects.all()
    serializer_class= PublisherSerializer

class PublisherDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Publisher.objects.all()
    serializer_class=PublisherSerializer