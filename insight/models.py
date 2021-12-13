from django.db import models

# Create your models here.

def insight_generate_id():
    try:
        id=Insight.objects.count()
        if id is not None:
            return f"DCB{1001+id}"
        else:
            return f"DCB{1001}"
    except Exception as e:
        print(e)

class Insight(models.Model):
   # overview_graph=models
   id=models.CharField(max_length=10,default=insight_generate_id,primary_key=True,editable=False)
   total_project=models.IntegerField()
   total_project_value=models.FloatField()
   total_project_amount_due=models.FloatField()
   timeline=models.DateField(null=True,blank=True)
   time=models.TimeField(null=True,blank=True)
   created_at=models.DateTimeField(auto_now_add=True)
   updated_at=models.DateTimeField(auto_now=True)
   #  def __str__(self):
   #     return self.total_project

   class Meta:
       verbose_name_plural='Insight'