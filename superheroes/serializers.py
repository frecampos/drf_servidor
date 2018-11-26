from rest_framework import serializers
from .models import Publisher,SuperHeroe

class SuperHeroeSerializer(serializers.ModelSerializer):
    class Meta:
        model= SuperHeroe
        fields = ('id','name','gender','real_name','publisher')

class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model= Publisher
        fields =('id','name','founder')