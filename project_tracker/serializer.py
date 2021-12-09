#from django.db.models import fields
from .models import *
from rest_framework import serializers

#Serializer for project Tracker
class ProjecTrackeSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProjectTracker
        fields=('excavation','foundation','plinth_stage',
        'gf_brick_work','gf_slab','first_floor_brick_work',
        'first_slab','electrical_works','plumbing_works','wood_grill_works',
        'internal_plastering','external_plastering','flooring_tiling','painting','finishing','calculate_percentage')
    
