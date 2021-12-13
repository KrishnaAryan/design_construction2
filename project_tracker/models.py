from django.db import models
from accounts.models import *
# Create your models here.

#creating a id for project_tracker
def project_tracker_generate_id():
    try:
        id=ProjectTracker.objects.count()
        if id is not None:
            return f"DCB{1001+id}"
        else:
            return f"DCB{1001}"
    except Exception as e:
        print(e)
#creating model for Project_tracker
class ProjectTracker(models.Model):
    id=models.CharField(max_length=10,default=project_tracker_generate_id,primary_key=True,editable=False)
    username=models.ForeignKey(Registration,related_name='project_tracker',on_delete=models.CASCADE)
    project=models.ForeignKey(ProjectDetails,related_name='projecttracker',on_delete=models.CASCADE)
    excavation=models.FloatField()
    foundation=models.FloatField()
    plinth_stage=models.FloatField()
    gf_brick_work=models.FloatField()
    gf_slab=models.FloatField()
    first_floor_brick_work=models.FloatField()
    first_slab=models.FloatField()
    electrical_works=models.FloatField()
    plumbing_works=models.FloatField()
    wood_grill_works=models.FloatField()
    internal_plastering=models.FloatField()
    external_plastering=models.FloatField()
    flooring_tiling=models.FloatField()
    painting=models.FloatField()
    finishing=models.FloatField()

    def __str__(self):
        return self.id

    class Meta:
        verbose_name_plural='Project Tracker'

    def calculate_percentage(self):
        #print(self.finishing,type(self.finishing))
        #return self.finishing+self.flooring_tiling
        sum=(self.excavation+self.foundation+self.plinth_stage
        +self.gf_brick_work+self.gf_slab+self.first_floor_brick_work+
        self.first_slab+self.electrical_works+self.plumbing_works+
        self.wood_grill_works+self.internal_plastering+self.external_plastering+
        self.flooring_tiling+self.painting+self.finishing)
        print(sum)
        p= sum/15
        return p/100

    def get_excavation(self):
        return self.excavation/100

    def get_foundation(self):
        return self.foundation/100

    def get_plinth_stage(self):
        return self.plinth_stage/100

    def get_gf_brick_work(self):
        return self.gf_brick_work/100

    def get_gf_slab(self):
        return self.gf_slab/100

    def get_first_floor_brick_work(self):
        return self.first_floor_brick_work/100

    def get_first_slab(self):
        return self.first_slab/100

    def get_electrical_works(self):
        return self.electrical_works/100

    def get_plumbing_works(self):
        return self.plumbing_works/100

    def get_wood_grill_works(self):
        return self.wood_grill_works/100

    def get_internal_plastering(self):
        return self.internal_plastering/100

    def get_external_plastering(self):
        return self.foundation/100

    def get_flooring_tiling(self):
        return self.foundation/100

    def get_painting(self):
        return self.painting/100

    def get_finishing(self):
        return self.finishing/100

