from .models import *
from rest_framework import serializers

class ProjecTrackeSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProjectTracker
        exclude=('username','project')
