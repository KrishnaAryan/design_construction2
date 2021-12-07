from django.db import models
from django.dispatch import receiver
from accounts.models import *
# Create your models here.
def payment_tracker_generate_id():
    try:
        id=PaymentTracker.objects.count()
        if id is not None:
            return f"DCB{1001+id}"
        else:
            return f"{1001}"

    except Exception as e:
        print(e)

class PaymentTracker(models.Model):
    user=models.ForeignKey(Registration,related_name='payment_tracker',on_delete=models.CASCADE)
    id=models.CharField(max_length=10,default=payment_tracker_generate_id,primary_key=True,editable=False)
    total_project_value=models.DecimalField(max_digits=10, decimal_places=2)
    total_paid=models.DecimalField(max_digits=10,decimal_places=2)
    total_amount_due=models.DecimalField(max_digits=10,decimal_places=2)
    payment_mode=models.CharField(max_length=100)


class PaymentInstallment(models.Model):
    user=models.ForeignKey(Registration,related_name='payment_installment',on_delete=models.CASCADE)
    project=models.ForeignKey(ProjectDetails,related_name='project',on_delete=models.CASCADE)
    amount=models.FloatField()
    installment=models.CharField(max_length=50,null=True,blank=True)
    date=models.DateField()
    payment_mode=models.CharField(max_length=50)
    status=models.BooleanField(default=False)

    



