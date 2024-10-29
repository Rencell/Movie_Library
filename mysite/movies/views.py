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
        data = serializer.data
        image_url = data.get('image')
        
        if image_url:
            file_name = os.path.basename(image_url)
            file_path = os.path.join(settings.MEDIA_ROOT, "Images" ,file_name)
            
            if os.path.exists(file_path):
                os.remove(file_path)
            
        return super().destroy(request, *args, **kwargs)
    
class ActionViewSet(viewsets.ModelViewSet):
    
    queryset = MovieData.objects.filter(typ='action')
    serializer_class = MovieSerializer
    
class ComedyViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.filter(typ='comedy')
    serializer_class = MovieSerializer