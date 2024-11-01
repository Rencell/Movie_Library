from rest_framework import serializers
from .models import MovieData
import os

class MovieSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None,use_url=True)
    class Meta:
        model = MovieData
        fields = ['id', 'name', 'duration', 'rating', 'typ','image']
    
    def delete(self, instance):
        if instance.image and os.path.isfile(instance.image.path):
            print(instance.image.path)
            os.remove(instance.image.path)
            
    def update(self, instance, validatedData):
        
        if instance.image and os.path.isfile(instance.image.path):
            if 'image' in validatedData:
                os.remove(instance.image.path)
                instance.image = validatedData['image']    
                instance.save()
                return instance
            else:
                instance.name = validatedData['name']
                instance.typ = validatedData['typ']
                instance.save()
                return instance    
        
    
        
        