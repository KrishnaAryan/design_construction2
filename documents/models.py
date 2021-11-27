from django.db import models
from django.contrib.auth.models import AbstractUser
from accounts.models import *
# Create your models here.
class Agreements(models.Model):
    booking_agreements=models.ImageField(upload_to='image/')
    main_agreements=models.ImageField(upload_to='image/')
    project_details=models.ForeignKey(ProjectDetails,related_name='agreements',on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
class Documents(models.Model):
    boq=models.ImageField(upload_to='image/')
    payments=models.ImageField(upload_to='image/')
    projects_schedule=models.ImageField(upload_to='image/')
    quality_checkList=models.ImageField(upload_to='image/')
    specifications=models.ImageField(upload_to='image/')
    project_details=models.ForeignKey(ProjectDetails,related_name='documents',on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
class ConceptPlans(models.Model):
    concept_plans=models.ImageField(upload_to='image/')
    project_details=models.ForeignKey(ProjectDetails,related_name='concept_plans',on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
class WorkingDrawings(models.Model):
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
    
class StructuralDrawings(models.Model):
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
    

class ThreeD(models.Model):
    three_d_elevation=models.ImageField(upload_to='image/')
    project_details=models.ForeignKey(ProjectDetails,related_name='three_d',on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    