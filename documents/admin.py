from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Agreements)
class AgreementsAdmin(admin.ModelAdmin):
    list_display=['id','booking_agreements','main_agreements','project_details','created_at','updated_at']
    list_per_page=10
    search_fields = ('id',)

@admin.register(Documents)
class DocumentsAdmin(admin.ModelAdmin):
    list_display=['id','boq','payments','projects_schedule','quality_checkList','specifications','project_details','created_at','updated_at']
    list_per_page=10
    search_fields = ('id',)

@admin.register(ConceptPlans)
class ConceptPlansAdmin(admin.ModelAdmin):
    list_display=['id','concept_plans','project_details','created_at','updated_at']
    list_per_page=10
    search_fields = ('id',)

@admin.register(WorkingDrawings)
class WorkingDrawingsAdmin(admin.ModelAdmin):
    list_display=['id','open_schedule','joinery_details','plumbing_details','electrical','section','section_elevation','toilet_detailing','brick_work_layout','project_details','created_at','updated_at']
    list_per_page=10
    search_fields = ('id',)

@admin.register(StructuralDrawings)
class StructuralDrawingsAdmin(admin.ModelAdmin):
    list_display=['id','center_line_plan','footing_layout','column_details','plinth_beam_details','beam_layout','slab_details','staircase_details','project_details','created_at','updated_at']
    list_per_page=10
    search_fields = ('id',)

@admin.register(ThreeD)
class ThreeDAdmin(admin.ModelAdmin):
    list_display=['id','three_d_elevation','project_details','created_at','updated_at']
    list_per_page=10
    search_fields = ('id',)