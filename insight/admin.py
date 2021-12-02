from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Insight)
class InsightAdmin(admin.ModelAdmin):
    list_display=['id','total_project','total_project_value','total_project_amount_due','timeline','time','created_at','updated_at']
    list_per_page=10
    search_fields = ('total_project','total_project_amount_due')
    list_filter=('total_project','total_project_amount_due',)
