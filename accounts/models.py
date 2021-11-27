from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import pre_save
from django.dispatch import receiver

# Create your models here.
class Registration(AbstractUser):
    mobile_no=models.CharField(max_length=13)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.mobile_no

@receiver(pre_save, sender=Registration)
def my_handler(sender,**kwargs):
    obj=kwargs['instance']
    password=obj.password
    obj.set_password(password)

class PersonalDetails(models.Model):
    registrations=models.ForeignKey(Registration,related_name='personal_details',on_delete=models.CASCADE)
    gender=models.CharField(max_length=10,choices=(('Male','Male'),('Female','Female')))
    dob=models.DateField()
    profile_image=models.ImageField(upload_to='image/')
    local_address=models.CharField(max_length=100)
    city=models.CharField(max_length=25)
    state=models.CharField(max_length=25)
    zip_code=models.CharField(max_length=6)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.city
    
class Package(models.Model):
    package_names=models.CharField(max_length=50)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.package_names

class ProjectDetails(models.Model):
    registration=models.ForeignKey(Registration,related_name='project_details',on_delete=models.CASCADE)
    booking_date=models.DateField()
    total_value=models.FloatField()
    booking_amount=models.FloatField()
    project_description=models.CharField(max_length=1000)
    package=models.ForeignKey(Package,related_name='project_details',on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.project_description

class Team(models.Model):
    team_name=models.CharField(max_length=25)
    project_details=models.ForeignKey(ProjectDetails,related_name='team',on_delete=models.CASCADE)
    project_head=models.CharField(max_length=25)
    project_manager=models.CharField(max_length=25)
    architect=models.CharField(max_length=25)
    structural_engineer=models.CharField(max_length=25)
    procurement_manager=models.CharField(max_length=25)
    project_coordinator=models.CharField(max_length=25)
    project_engineer=models.CharField(max_length=25)
    site_engineer=models.CharField(max_length=25)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.team_name