from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Finance)
class FinanceAdmin(admin.ModelAdmin):
    list_display=('emp_name','emp_id','designation','project_details')
    list_per_page=10
    search_fields = ('emp_name','emp_id')

@admin.register(ProjectCoordination)
class ProjectCoordinationAdmin(admin.ModelAdmin):
    list_display=('emp_name','emp_id','designation','project_details')
    list_per_page=10
    search_fields = ('emp_name','emp_id')

@admin.register(DesignTeam)
class DesignTeamAdmin(admin.ModelAdmin):
    list_display=('emp_name','emp_id','designation','project_details')
    list_per_page=10
    search_fields = ('emp_name','emp_id')

@admin.register(ExecutionTeam)
class ExecutionTeamAdmin(admin.ModelAdmin):
    list_display=('emp_name','emp_id','designation','project_details')
    list_per_page=10
    search_fields = ('emp_name','emp_id')