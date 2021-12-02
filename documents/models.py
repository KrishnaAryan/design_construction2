from django.db import models
from django.contrib.auth.models import AbstractUser
from accounts.models import *
# Create your models here.
def agreement_generate_id():
    try:
        obj=Agreements.objects.last()
        if obj is not None:
            return (obj.id)+1
        else:
            return 1001
    except Exception as e:
        print(e)

class Agreements(models.Model):
    id=models.IntegerField(default=agreement_generate_id,primary_key=True,editable=False)
    booking_agreements=models.ImageField(upload_to='image/')
    main_agreements=models.ImageField(upload_to='image/')
    project_details=models.ForeignKey(ProjectDetails,related_name='agreements',on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

def document_generate_id():
    try:
        obj=Documents.objects.last()
        if obj is not None:
            return (obj.id)+1
        else:
            return 1001
    except Exception as e:
        print(e)

class Documents(models.Model):
    id=models.IntegerField(default=document_generate_id,primary_key=True,editable=False)
    boq=models.ImageField(upload_to='image/')
    payments=models.ImageField(upload_to='image/')
    projects_schedule=models.ImageField(upload_to='image/')
    quality_checkList=models.ImageField(upload_to='image/')
    specifications=models.ImageField(upload_to='image/')
    project_details=models.ForeignKey(ProjectDetails,related_name='documents',on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

def concept_plan_generate_id():
    try:
        obj=ConceptPlans.objects.last()
        if obj is not None:
            return (obj.id)+1
        else:
            return 1001
    except Exception as e:
        print(e)

class ConceptPlans(models.Model):
    id=models.IntegerField(default=concept_plan_generate_id,primary_key=True,editable=False)
    concept_plans=models.ImageField(upload_to='image/')
    project_details=models.ForeignKey(ProjectDetails,related_name='concept_plans',on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

def working_drawings_generate_id():
    try:
        obj=WorkingDrawings.objects.last()
        if obj is not None:
            return (obj.id)+1
        else:
            return 1001
    except Exception as e:
        print(e)

class WorkingDrawings(models.Model):
    id=models.IntegerField(default=working_drawings_generate_id,primary_key=True,editable=False)
    open_schedule=models.ImageField(upload_to='image/')
    joinery_details=models.ImageField(upload_to='image/')
    plumbing_details=models.ImageField(upload_to='image/')
    electrical=models.ImageField(upload_to='image/')
    section=models.ImageField(upload_to='image/')
    section_elevation=models.ImageField(upload_to='image/')
    toilet_detailing=models.ImageField(upload_to='image/')
    brick_work_layout=models.ImageField(upload_to='image/')
    project_details=models.ForeignKey(ProjectDetails,related_name='workingdrawings',on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

def structural_drawing_generate_id():
    try:
        obj=StructuralDrawings.objects.last()
        if obj is not None:
            return (obj.id)+1
        else:
            return 1001
    except Exception as e:
        print(e)

class StructuralDrawings(models.Model):
    id=models.IntegerField(default=structural_drawing_generate_id,primary_key=True,editable=False)
    center_line_plan=models.ImageField(upload_to='image/')
    footing_layout=models.ImageField(upload_to='image/')
    column_details=models.ImageField(upload_to='image/')
    plinth_beam_details=models.ImageField(upload_to='image/')
    beam_layout=models.ImageField(upload_to='image/')
    beam_details=models.ImageField(upload_to='image/')
    slab_details=models.ImageField(upload_to='image/')
    staircase_details=models.ImageField(upload_to='image/')
    project_details=models.ForeignKey(ProjectDetails,related_name='structural_drawings',on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
def three_generate_id():
    try:
        obj=ThreeD.objects.last()
        if obj is not None:
            return (obj.id)+1
        else:
            return 1001
    except Exception as e:
        print(e)

class ThreeD(models.Model):
    id=models.IntegerField(default=three_generate_id,primary_key=True,editable=False)
    three_d_elevation=models.ImageField(upload_to='image/')
    project_details=models.ForeignKey(ProjectDetails,related_name='three_d',on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    