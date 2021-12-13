#from django.db.models import fields
from .models import *
from rest_framework import serializers

#Serializer for project Tracker
class ProjecTrackeSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProjectTracker
        fields=('get_excavation','get_foundation','get_plinth_stage',
        'get_gf_brick_work','get_gf_slab','get_first_floor_brick_work',
        'get_first_slab','get_electrical_works','get_plumbing_works','get_wood_grill_works',
        'get_internal_plastering','get_external_plastering','get_flooring_tiling','get_painting','get_finishing','calculate_percentage')
    
