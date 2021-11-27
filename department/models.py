from django.db import models
from django.contrib.auth.models import AbstractUser
from accounts.models import *

# Create your models here.
class Finance(models.Model):
    emp_name=models.CharField(max_length=25)
    emp_id=models.CharField(max_length=8)
    designation=models.CharField(max_length=15)
    project_details=models.ForeignKey(ProjectDetails,related_name='finance',on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.emp_name

class ProjectCoordination(models.Model):
    emp_name=models.CharField(max_length=25)
    emp_id=models.CharField(max_length=8)
    designation=models.CharField(max_length=15)
    project_details=models.ForeignKey(ProjectDetails,related_name='project_coordination',on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.emp_name

class DesignTeam(models.Model):
    emp_name=models.CharField(max_length=25)
    emp_id=models.CharField(max_length=8)
    designation=models.CharField(max_length=15)
    project_details=models.ForeignKey(ProjectDetails,related_name='design_team',on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.emp_name

class ExecutionTeam(models.Model):
    emp_name=models.CharField(max_length=25)
    emp_id=models.CharField(max_length=8)
    designation=models.CharField(max_length=15)
    project_details=models.ForeignKey(ProjectDetails,related_name='execution_team',on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.emp_name

