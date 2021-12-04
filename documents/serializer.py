
from django.db.models import fields
from .models import *
from rest_framework import serializers

class AgreementsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Agreements
        fields=('booking_agreements','main_agreements')

class DocumentsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Documents
        fields=('boq','payments','projects_schedule','quality_checkList','specifications')

class ConceptPlansSerializer(serializers.ModelSerializer):
    class Meta:
        model=ConceptPlans
        fields=('concept_plans',)

class WorkingDrawingsSerializer(serializers.ModelSerializer):
    class Meta:
        model=WorkingDrawings
        fields=('open_schedule','joinery_details','plumbing_details','electrical','section','section_elevation','toilet_detailing','brick_work_layout')

class StructuralDrawingsSerializer(serializers.ModelSerializer):
    class Meta:
        model=StructuralDrawings
        fields=('center_line_plan','footing_layout','column_details','plinth_beam_details','beam_layout','slab_details','staircase_details')

class ThreeDSerializer(serializers.ModelSerializer):
    class Meta:
        model=ThreeD
        fields=('three_d_elevation',)

class GalleryImageSerializer(serializers.ModelSerializer):
    class Meta:
        model=GalleryImage
        fields=('id','inside','outside','two_d_image','three_d_image')
