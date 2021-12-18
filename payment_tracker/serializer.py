
from django.db.models import fields
from .models import *
from rest_framework import serializers

class PaymentTrackerSerializer(serializers.ModelSerializer):
    class Meta:
        model=PaymentTracker
        fields=['id','total_project_value','total_paid','total_amount_due','payment_mode']


class PaymentInstallmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=PaymentInstallment
        exclude=('user','project')

class PaymetInstallmentSerializer1(serializers.ModelSerializer):
    payment_tracker =PaymentTrackerSerializer(read_only=True,many=True)
    payment_installment = PaymentInstallmentSerializer(read_only=True,many=True)
    class Meta:
        model=Registration
        fields=['id','mobile_no','payment_tracker','payment_installment']