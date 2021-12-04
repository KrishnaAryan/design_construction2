
from django.db.models import fields
from .models import *
from rest_framework import serializers

class FinanceSerializer(serializers.ModelSerializer):
    class Meta:
        model:Finance
        fields=['emp_name','emp_id','designation','project_details']

class ProjectCoordinationSerializer(serializers.ModelSerializer):
    class Meta:
        model:ProjectCoordination
        fields=['emp_name','emp_id','designation','project_details']

class DesignTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model=DesignTeam
        fields=['emp_name','emp_id','designation','project_details']

class ExecutionTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model=ExecutionTeam
        fields=['emp_name','emp_id','designation','project_details']