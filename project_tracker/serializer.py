from .models import *
from rest_framework import serializers

#Serializer for project Tracker
class ProjecTrackeSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProjectTracker
        exclude=('username','project')
