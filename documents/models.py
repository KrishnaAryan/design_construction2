from django.db import models
from django.contrib.auth.models import AbstractUser
from accounts.models import *
# Create your models here.
def agreement_generate_id():
    try:
        id=Agreements.objects.count()
        print(id)
        if id is not None:
            return f"DCB{1001+id}"
        else:
            return f"DCB{1001}"
    except Exception as e:
        print(e)

class Agreements(models.Model):
    id=models.CharField(max_length=10, default=agreement_generate_id,primary_key=True,editable=False)
    booking_agreements=models.ImageField(upload_to='image/')
    main_agreements=models.ImageField(upload_to='image/')
    project_details=models.ForeignKey(ProjectDetails,related_name='agreements',on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id

    class Meta:
        #verbose_name='agreement'
        verbose_name_plural='agreement'

def document_generate_id():
    try:
        id=Documents.objects.count()
        if id is not None:
            return f"DCB{1001+id}"
        else:
            return f"DCB{1001}"
    except Exception as e:
        print(e)

class Documents(models.Model):
    id=models.CharField(max_length=10, default=document_generate_id,primary_key=True,editable=False)
    boq=models.ImageField(upload_to='image/')
    payments=models.ImageField(upload_to='image/')
    projects_schedule=models.ImageField(upload_to='image/')
    quality_checkList=models.ImageField(upload_to='image/')
    specifications=models.ImageField(upload_to='image/')
    project_details=models.ForeignKey(ProjectDetails,related_name='documents',on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
        #verbose_name='document'
        verbose_name_plural='document'

def concept_plan_generate_id():
    try:
        id=ConceptPlans.objects.count()
        if id is not None:
            return f"DCB{1001+id}"
        else:
            return f"DCB{1001}"
    except Exception as e:
        print(e)

class ConceptPlans(models.Model):
    id=models.CharField(max_length=10, default=concept_plan_generate_id,primary_key=True,editable=False)
    concept_plans=models.ImageField(upload_to='image/')
    project_details=models.ForeignKey(ProjectDetails,related_name='concept_plans',on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
        #verbose_name='conceptplan'
        verbose_name_plural='concept Plan'

def working_drawings_generate_id():
    try:
        id=WorkingDrawings.objects.count()
        if id is not None:
            return f"DCB{1001+id}"
        else:
            return f"DCB{1001}"
    except Exception as e:
        print(e)


class WorkingDrawings(models.Model):
    id=models.CharField(max_length=10, default=working_drawings_generate_id,primary_key=True,editable=False)
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

    class Meta:
        #verbose_name='workingdrawing'
        verbose_name_plural='working Drawing'

def structural_drawing_generate_id():
    try:
        id=StructuralDrawings.objects.count()
        if id is not None:
            return f"DCB{1001+id}"
        else:
            return f"DCB{1001}"
    except Exception as e:
        print(e)

class StructuralDrawings(models.Model):
    id=models.CharField(max_length=10, default=structural_drawing_generate_id,primary_key=True,editable=False)
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

    class Meta:
        #verbose_name='structuraldrawing'
        verbose_name_plural='structural Drawing'
    
def three_generate_id():
    try:
        id=ThreeD.objects.count()
        if id is not None:
            return f"DCB{1001+id}"
        else:
            return f"DCB{1001}"
    except Exception as e:
        print(e)

class ThreeDModel(models.Model):
    id=models.CharField(max_length=10, default=three_generate_id,primary_key=True,editable=False)
    three_d_elevation=models.ImageField(upload_to='image/')
    project_details=models.ForeignKey(ProjectDetails,related_name='three_d',on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    
    class Meta:
        verbose_name_plural='Three-D Image'


def gallery_generate_id():
    try:
        id=GalleryImage.objects.count()
        if id is not None:
            return f"DCB{1001+id}"
        else:
            return f"DCB{1001}"
    except Exception as e:
        print(e)
class GalleryImage(models.Model):
    user_name=models.ForeignKey(Registration,related_name='user_name',on_delete=models.CASCADE)
    project_details=models.ForeignKey(ProjectDetails,related_name='gallery',on_delete=models.CASCADE)
    id=models.CharField(max_length=10, default=gallery_generate_id,primary_key=True,editable=False)
    # inside=models.ImageField(upload_to='inside/')
    # outside=models.Im(upload_to='outside/')
    # two_d_image=models.ImageField(upload_to='two_d/')
    # three_d_image=models.ImageField(upload_to='three_d/')

    class Meta:
        verbose_name_plural='Gallery Image'

class InsideImage(models.Model):
    gallery_image=models.ForeignKey(GalleryImage,related_name='inside',on_delete=models.CASCADE)
    inside=models.ImageField(upload_to='inside/')
    class Meta:
        verbose_name_plural='Inside Image'

class OutsideImage(models.Model):
    gallery_image=models.ForeignKey(GalleryImage,related_name='outside',on_delete=models.CASCADE)
    outside=models.ImageField(upload_to='outside/')
    class Meta:
        verbose_name_plural='Outside Image'

class TwoD(models.Model):
    gallery_image=models.ForeignKey(GalleryImage,related_name='two_d',on_delete=models.CASCADE)
    two_d=models.ImageField(upload_to='two_d/')
    class Meta:
        verbose_name_plural='Two-D'

class ThreeD(models.Model):
    gallery_image=models.ForeignKey(GalleryImage,related_name='three_d',on_delete=models.CASCADE)
    three_d=models.ImageField(upload_to='three_d/')
    class Meta:
        verbose_name_plural='Three-D'

