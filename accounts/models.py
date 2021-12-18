from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.db.models import Sum
from django.db.models.signals import post_save
from django.dispatch import receiver
from .sendMail import *
# Create your models here.
def customer_generate_id():
    try:
        id=Registration.objects.count()
        if id is not None:
            return f"DCB{1001+id}"
        else:
            return f"DCB{1001}"
    except Exception as e:
        print(e)

class Registration(AbstractUser):

    """It is store data into registration table"""
    first_name=None
    last_name=None
    id=models.CharField(max_length=10, default=customer_generate_id,primary_key=True,editable=False)
    mobile_no=models.CharField(max_length=13)
    #email=models.EmailField(unique=True)
    otp=models.IntegerField(default=0)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.username

    class Meta:
        # verbose_name='user'
        verbose_name_plural='user'
    
    # def save(self):
    #     user = super(self,Registration)
    #     print("sandeep",user)
    #     user.set_password(self.password)
    #     user.save()
    #     return user

# @receiver(pre_save, sender=Registration)
# def encript_password(sender,**kwargs):

#     """This function is used to encript password"""

#     obj=kwargs['instance']
#     password=obj.password
#     obj.set_password(password)
    #obj.save()
def personal_generate_id():
    try:
        id=PersonalDetails.objects.count()
        if id is not None:
            return f"DCB{1001+id}"
        else:
            return f"DCB{1001}"
    except Exception as e:
        print(e)

class PersonalDetails(models.Model):

    """This model is used to stores personal details into table"""

    registrations=models.ForeignKey(Registration,related_name='personal_details',on_delete=models.CASCADE)
    id=models.CharField(max_length=10, default=personal_generate_id,primary_key=True,editable=False)
    full_name=models.CharField(max_length=100,null=True,blank=True)
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
        return self.full_name

    class Meta:
        #verbose_name='personaldetail'
        verbose_name_plural='personal Detail'
    
def package_generate_id():
    try:
        id=Package.objects.count()
        if id is not None:
            return f"DCB{1001+id}"
        else:
            return f"DCB{1001}"
    except Exception as e:
        print(e)

class Package(models.Model):

    """This model is used to store package into table"""
    id=models.CharField(max_length=10,default=package_generate_id,primary_key=True,editable=False)
    package_names=models.CharField(max_length=50)
    package_detail=models.TextField(null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.package_names

    class Meta:
        verbose_name_plural='Package'

def department_generate_id():
    try:
        id=Department.objects.count()
        if id is not None:
            return f"DCB{1001+id}"
        else:
            return f"DCB{1001}"
    except Exception as e:
        print(e)

class Department(models.Model):
    id=models.CharField(max_length=10,default=department_generate_id,primary_key=True,editable=False)
    department_name=models.CharField(max_length=100,)
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.department_name

    class Meta:
        verbose_name_plural='Department'

def projectDetails_generate_id():
    try:
        id=ProjectDetails.objects.count()
        if id is not None:
            return f"DCB{1001+id}"
        else:
            return f"DCB{1001}"
    except Exception as e:
        print(e)

class ProjectDetails(models.Model):

    """This model is used to store project details into table"""

    registration=models.ForeignKey(Registration,related_name='project_details',on_delete=models.CASCADE)
    department=models.ForeignKey(Department,related_name='department',on_delete=models.CASCADE)
    id=models.CharField(max_length=10, default=projectDetails_generate_id,primary_key=True,editable=False)
    booking_date=models.DateField()
    total_value=models.FloatField()
    booking_amount=models.FloatField()
    project_description=models.TextField(max_length=1000)
    package=models.ForeignKey(Package,related_name='project_details',on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id
    def totalValue(self):
        total_value=self.objects.aggregate(Sum('total_value'))
        return total_value
    def totalAmount(self):
        total_amount=self.objects.aggregate(Sum('booking_amount'))
        return total_amount

    class Meta:
        #verbose_name='projectdetail'
        verbose_name_plural='project Detail'
        




def team_generate_id():
    try:
        id=Team.objects.count()
        if id is not None:
            return f"DCB{1001+id}"
        else:
            return f"DCB{1001}"
    except Exception as e:
        print(e)

class Team(models.Model):

    """This model is used store team into table"""

    registration=models.ForeignKey(Registration,related_name='register',on_delete=models.CASCADE,null=True,blank=True)
    project_details=models.ForeignKey(ProjectDetails,related_name='team',on_delete=models.CASCADE)
    id=models.CharField(max_length=10, default=team_generate_id,primary_key=True,editable=False)
    name=models.CharField(max_length=25)
    position=models.CharField(max_length=100,null=True,blank=True)
    mobile_number=models.CharField(max_length=100,null=True,blank=True)
    profile_pic=models.ImageField(upload_to='profile/',null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural='Team'


class Notification(models.Model):
    user=models.ForeignKey(Registration,on_delete=models.CASCADE)
    subject=models.CharField(max_length=50)
    message=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)



@receiver(post_save,sender=Notification)
def send_notification(sender,instance,**kwargs):
    obj=instance.user
    email=obj.email
    send_notification_on_email(email,instance.subject,instance.message)
    
    # def save()