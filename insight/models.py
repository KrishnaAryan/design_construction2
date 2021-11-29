from django.db import models

# Create your models here.
class Insight(models.Model):
   # overview_graph=models
    total_project=models.IntegerField()
    total_project_value=models.FloatField()
    total_project_amount_due=models.FloatField()
    timeline=models.DateField(null=True,blank=True)
    time=models.TimeField(null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
   #  def __str__(self):
   #     return self.total_project