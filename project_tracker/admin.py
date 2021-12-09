from django.contrib import admin
from .models import *
# Register your models here.
#all data showing in admin section
@admin.register(ProjectTracker)
class ProjectTrackerAdmin(admin.ModelAdmin):
    list_display=('id','username','project','excavation','calculate_percentage','foundation','plinth_stage',
                'gf_brick_work','gf_slab','first_floor_brick_work','first_slab',
                'electrical_works','plumbing_works','wood_grill_works','internal_plastering',
                'external_plastering','flooring_tiling','painting','finishing')

    fields=(('username','project'),('excavation','foundation'),('plinth_stage',
                'gf_brick_work'),('gf_slab','first_floor_brick_work'),('first_slab',
                'electrical_works'),('plumbing_works','wood_grill_works'),('internal_plastering',
                'external_plastering'),('flooring_tiling','painting'),('finishing',))