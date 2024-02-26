from rest_framework import serializers

from app import models

class ProjectSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Project
        fields = '__all__'
        
class ActionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Action
        fields = '__all__'
        
class IndicatorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Indicator
        fields = '__all__'