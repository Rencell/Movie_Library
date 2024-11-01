from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MovieSerializer
from .models import MovieData
from django.conf import settings
import os
# Create your views here.
class MovieViewSet(viewsets.ModelViewSet):
    
    queryset = MovieData.objects.all()
    serializer_class = MovieSerializer
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        
        serializer = self.get_serializer(instance)
        serializer.delete(instance)
       
        return super().destroy(request, *args, **kwargs)
    
    
    
    
class ActionViewSet(viewsets.ModelViewSet):
    
    queryset = MovieData.objects.filter(typ='action')
    serializer_class = MovieSerializer
    
class ComedyViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.filter(typ='comedy')
    serializer_class = MovieSerializer