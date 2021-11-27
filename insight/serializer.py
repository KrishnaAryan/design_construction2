
from django.db.models import fields
from .models import *
from rest_framework import serializers

class InsightSerializer(serializers.ModelSerializer):
    class Meta:
        model=Insight
        fields=['total_project','total_project_value','total_project_amount_due','timeline']