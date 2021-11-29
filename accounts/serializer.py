
from django.db.models import fields
from .models import *
from rest_framework import serializers

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Registration
        fields=['first_name','last_name','email','username','password','mobile_no']

    def create(self, validated_data):
        password=validated_data['password']
        obj=Registration.objects.create(
            username=validated_data['username'],
            mobile_no=validated_data['mobile_no'],
            password=password
        )
        obj.set_password(password)
        obj.save()
        return obj

class LoginSerializer(serializers.Serializer):
    username=serializers.CharField(required=True)
    password=serializers.CharField(required=True)

class ChangePasswordSerializer(serializers.Serializer):
    password=serializers.CharField(required=True)
    new_password=serializers.CharField(required=True)

class PersonalDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model=PersonalDetails
        fields=['registrations','gender','dob','profile_image','local_address','city','state','zip_code']

class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model=Package
        fields=['package_names','created_at','updated_at']

class ProjectDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProjectDetails
        fields=['registration','booking_date','total_value','booking_amount','project_description','package']

class ProjectDetailsSerilizer1(serializers.ModelSerializer):
    package=PackageSerializer()
    class Meta:
        model=ProjectDetails
        fields=['registration','booking_date','total_value',
                'booking_amount','project_description','package']
                
class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model=Team
        fields=['team_name','project_details','project_head','project_manager','architect','structural_engineer','procurement_manager','project_coordinator','project_engineer','site_engineer']

""" ProjectDetails use for geting data in Registration """
class CustomerRegistrationSerializer1(serializers.ModelSerializer):
    projectdetails=ProjectDetailsSerializer(read_only=True,many=True)
    class Meta:
        model=Registration
        fields=['projectdetails']
