from django.db import models
from django.contrib.auth.models import AbstractUser
from accounts.models import *

# Create your models here.
def generate_finance_id():
    id=Finance.objects.count()
    if id is not None:
        return f"DCB{1001+id}"
    else:
        return f"DCB{1001}"

class Finance(models.Model):
    emp_name=models.CharField(max_length=25)
    emp_id=models.CharField(max_length=10,default=generate_finance_id,primary_key=True,editable=False)
    designation=models.CharField(max_length=15)
    project_details=models.ForeignKey(ProjectDetails,related_name='finance',on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.emp_name

    class Meta:
        verbose_name_plural='Finance'

def project_coordination_id():
    id=ProjectCoordination.objects.count()
    if id is not None:
        return f"DCB{1001+id}"
    else:
        return f"DCB{1001}"

class ProjectCoordination(models.Model):
    emp_name=models.CharField(max_length=25)
    emp_id=models.CharField(max_length=10,default=project_coordination_id,primary_key=True,editable=False)
    designation=models.CharField(max_length=15)
    project_details=models.ForeignKey(ProjectDetails,related_name='project_coordination',on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.emp_name

    class Meta:
        verbose_name_plural='Project Coordination'


def design_team_id():
    id=DesignTeam.objects.count()
    if id is not None:
        return f"DCB{1001+id}"
    else:
        return f"DCB{1001}"

class DesignTeam(models.Model):
    emp_name=models.CharField(max_length=25)
    emp_id=models.CharField(max_length=10,default=design_team_id,primary_key=True,editable=False)
    designation=models.CharField(max_length=15)
    project_details=models.ForeignKey(ProjectDetails,related_name='design_team',on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.emp_name

    class Meta:
        verbose_name_plural='Design Team'


def execution_team_id():
    id=ExecutionTeam.objects.count()
    if id is not None:
        return f"DCB{1001+id}"
    else:
        return f"DCB{1001}"

class ExecutionTeam(models.Model):
    emp_name=models.CharField(max_length=25)
    emp_id=models.CharField(max_length=10,default=execution_team_id,primary_key=True,editable=False)
    designation=models.CharField(max_length=15)
    project_details=models.ForeignKey(ProjectDetails,related_name='execution_team',on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.emp_name

    class Meta:
        verbose_name_plural='Execution Team'



