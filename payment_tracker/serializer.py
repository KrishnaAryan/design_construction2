
from django.db.models import fields
from .models import *
from rest_framework import serializers

class PaymentTrackerSerializer(serializers.ModelSerializer):
    class Meta:
        model=PaymentTracker
        fields=['id','total_project_value','total_paid','total_amount_due','payment_mode']

