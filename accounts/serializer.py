
from django.db.models import fields

from documents.serializer import DocumentsSerializer
from .models import *
from rest_framework import serializers

class RegistrationSerializer(serializers.ModelSerializer):
    email=serializers.EmailField(required=True)
    class Meta:
        model=Registration
        fields=['id','email','username','password','mobile_no']

    def create(self, validated_data):
        password=validated_data['password']
        obj=Registration.objects.create(
            username=validated_data['username'],
            mobile_no=validated_data['mobile_no'],
            email=validated_data['email'],
            password=password
        )
        obj.set_password(password)
        obj.save()
        return obj

class RegistrationSerializer1(serializers.ModelSerializer):
    class Meta:
        model=Registration
        fields=['first_name','last_name','email']

class LoginSerializer(serializers.Serializer):
    username=serializers.CharField(required=True)
    password=serializers.CharField(required=True)

class ChangePasswordSerializer(serializers.Serializer):
    password=serializers.CharField(required=True)
    new_password=serializers.CharField(required=True)

class PersonalDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model=PersonalDetails
        fields=['full_name','gender','dob','profile_image','local_address','city','state','zip_code']

class PersonalDetailsSerializer1(serializers.ModelSerializer):
    registrations=RegistrationSerializer()
    class Meta:
        model=PersonalDetails
        fields=['registrations','full_name','gender','dob','profile_image','local_address','city','state','zip_code']


class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model=Package
        fields=('package_names','package_detail')

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Department
        fields=('department_name','name')

class ProjectDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProjectDetails
        fields=['id','registration','department','booking_date','total_value','booking_amount','project_description','package']

class ProjectDetailsSerilizer1(serializers.ModelSerializer):
    package=PackageSerializer()
    department=DepartmentSerializer()
    class Meta:
        model=ProjectDetails
        fields=['id','booking_date','total_value',
                'booking_amount','project_description','department','package']
                
class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model=Team
        fields=['name','position','mobile_number','profile_pic']

class TeamSerializer1(serializers.ModelSerializer):
    
    class Meta:
        model=Team
        fields=['id','registration','project_details','name','position','mobile_number','profile_pic']


""" ProjectDetails use for geting data in Registration """
class CustomerRegistrationSerializer1(serializers.ModelSerializer):
    projectdetails=ProjectDetailsSerializer(read_only=True,many=True)
    class Meta:
        model=Registration
        fields=['projectdetails']


"""All Related data get in a single Project"""
class SingleProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProjectDetails
        fields=['id','booking_date','total_value','booking_amount','project_description','package','created_at','team',
      'registration','documents']


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'