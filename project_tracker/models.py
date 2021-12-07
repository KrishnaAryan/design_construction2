from django.db import models
from accounts.models import *
# Create your models here.

def project_tracker_generate_id():
    try:
        id=ProjectTracker.objects.count()
        if id is not None:
            return f"DCB{1001+id}"
        else:
            return f"DCB{1001}"
    except Exception as e:
        print(e)

class ProjectTracker(models.Model):
    id=models.CharField(max_length=10,default=project_tracker_generate_id,primary_key=True,editable=False)
    username=models.ForeignKey(Registration,related_name='project_tracker',on_delete=models.CASCADE)
    project=models.ForeignKey(ProjectDetails,related_name='projecttracker',on_delete=models.CASCADE)
    excavation=models.CharField(max_length=5)
    foundation=models.CharField(max_length=5)
    plinth_stage=models.CharField(max_length=5)
    gf_brick_work=models.CharField(max_length=5)
    gf_slab=models.CharField(max_length=5)
    first_floor_brick_work=models.CharField(max_length=5)
    first_slab=models.CharField(max_length=5)
    electrical_works=models.CharField(max_length=5)
    plumbing_works=models.CharField(max_length=5)
    wood_grill_works=models.CharField(max_length=5)
    internal_plastering=models.CharField(max_length=5)
    external_plastering=models.CharField(max_length=5)
    flooring_tiling=models.CharField(max_length=5)
    painting=models.CharField(max_length=5)
    finishing=models.CharField(max_length=5)

    def __str__(self):
        return self.excavation

