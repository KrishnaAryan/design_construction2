from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(PaymentTracker)
class PackageAdmin(admin.ModelAdmin):
    list_display=('id','user','total_project_value','total_paid','total_amount_due','payment_mode')
    search_fields = ('user__username',)
    list_per_page=10
