from django.db import models
from django.contrib.auth.models import AbstractUser
from accounts.models import *

# Create your models here.
def generate_finance_id():
    obj=Finance.objects.last()
    if obj is not None:
        return obj.emp_id+1
    else:
        return 1001

class Finance(models.Model):
    emp_name=models.CharField(max_length=25)
    emp_id=models.IntegerField(default=generate_finance_id,primary_key=True,editable=False)
    designation=models.CharField(max_length=15)
    project_details=models.ForeignKey(ProjectDetails,related_name='finance',on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.emp_name

def project_coordination_id():
    obj=ProjectCoordination.objects.last()
    if obj is not None:
        return obj.emp_id+1
    else:
        return 1001

class ProjectCoordination(models.Model):
    emp_name=models.CharField(max_length=25)
    emp_id=models.IntegerField(default=project_coordination_id,primary_key=True,editable=False)
    designation=models.CharField(max_length=15)
    project_details=models.ForeignKey(ProjectDetails,related_name='project_coordination',on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.emp_name


def design_team_id():
    obj=DesignTeam.objects.last()
    if obj is not None:
        return obj.emp_id+1
    else:
        return 1001

class DesignTeam(models.Model):
    emp_name=models.CharField(max_length=25)
    emp_id=models.IntegerField(default=design_team_id,primary_key=True,editable=False)
    designation=models.CharField(max_length=15)
    project_details=models.ForeignKey(ProjectDetails,related_name='design_team',on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.emp_name


def execution_team_id():
    obj=ExecutionTeam.objects.last()
    if obj is not None:
        return obj.emp_id+1
    else:
        return 1001

class ExecutionTeam(models.Model):
    emp_name=models.CharField(max_length=25)
    emp_id=models.IntegerField(default=execution_team_id,primary_key=True,editable=False)
    designation=models.CharField(max_length=15)
    project_details=models.ForeignKey(ProjectDetails,related_name='execution_team',on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.emp_name

