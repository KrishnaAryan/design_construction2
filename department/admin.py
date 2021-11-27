from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Finance)
class FinanceAdmin(admin.ModelAdmin):
    list_display=['emp_name','emp_id','designation','project_details','created_at','updated_at']

@admin.register(ProjectCoordination)
class ProjectCoordinationAdmin(admin.ModelAdmin):
    list_display=['emp_name','emp_id','designation','project_details','created_at','updated_at']

@admin.register(DesignTeam)
class DesignTeamAdmin(admin.ModelAdmin):
    list_display=['emp_name','emp_id','designation','project_details','created_at','updated_at']

@admin.register(ExecutionTeam)
class ExecutionTeamAdmin(admin.ModelAdmin):
    list_display=['emp_name','emp_id','designation','project_details','created_at','updated_at']

