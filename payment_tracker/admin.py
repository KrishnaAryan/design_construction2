from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(PaymentTracker)
class PackageAdmin(admin.ModelAdmin):
    list_display=('id','user','total_project_value','total_paid','due_amount','payment_mode')
    fields=('user','total_project_value','total_paid','payment_mode')
    search_fields = ('user',)
    list_per_page=10

    # def total_amount_paid(self,obj):
    #     if obj.total_paid >= obj.total_project_value:
    #         obj.save()
    #         print('successful amount')
    #     else:
    #         print('balance is over')

@admin.register(PaymentInstallment)
class Admin(admin.ModelAdmin):
    list_display=('id','user','project','amount','installment','date','payment_mode','status')
    fields=('user','project','amount','installment','date','payment_mode','status')
    search_fields = ('user',)
    list_per_page=10


    
