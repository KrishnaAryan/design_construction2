from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Insight)
class InsightAdmin(admin.ModelAdmin):
    list_display=['total_project','total_project_value','total_project_amount_due','timeline','created_at','updated_at']