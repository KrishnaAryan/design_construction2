from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.serializers import Serializer

from .testingSerializer import *
from .serializer import *
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth import authenticate
from django.contrib.auth import logout
import random
from .sendMail import *

# Create your views here.

"""This API is used to post data into database"""

class RegistrationView(APIView):
    def get(self,request):
        try:
            username=request.GET.get('username')
            if username:
                obj=Registration.objects.filter(username=username).first()
                if obj:
                    serializer=RegistrationSerializer(obj)
                    return Response(data=serializer.data,status=status.HTTP_200_OK)
                else:
                    return Response({'message':'Username not found'},status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print(e)
            return Response({'message':'Something went wrong'},status=status.HTTP_400_BAD_REQUEST)

    def post(self,request):
        try:
            data=request.data
            serializer=RegistrationSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data,status=status.HTTP_200_OK)
            else:
                return Response(data=serializer.errors,status=status.HTTP_406_NOT_ACCEPTABLE)
        except Exception as e:
            print(e)
            return Response({'message':'something went wrong'},status=status.HTTP_400_BAD_REQUEST)


    def patch(self,request):
        try:
            username=request.GET.get('username')
            data=request.data
            if username:
                obj=Registration.objects.filter(username=username).first()
                if obj:
                    serializer=RegistrationSerializer1(obj,data)
                    if serializer.is_valid():
                        serializer.save()
                        return Response(data=serializer.data,status=status.HTTP_200_OK)
                    else:
                        return Response(data=serializer.errors,status=status.HTTP_406_NOT_ACCEPTABLE)
                else:
                    return Response({'message':'Username not found'},status=status.HTTP_404_NOT_FOUND)
            else:
                return Response({'message':'Username is empty please provide username'},status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print(e)
            return Response({'message':'something went wrong'},status=status.HTTP_400_BAD_REQUEST)


""" This API is used to login from registration table """

class LoginView(APIView):
    def post(self,request):
        try:
            data=request.data
            serializer=LoginSerializer(data=data)
            if serializer.is_valid():
                username=serializer.data['username']
                password=serializer.data['password']
                register=Registration.objects.filter(username=username).first()
                if register:
                    if username and password:
                        user=authenticate(username=username,password=password)
                        if user:
                            return Response({
                                'message':'login successful'
                            },status=status.HTTP_200_OK)
                        else:
                            return Response({'message':'Invalid username and password'},status=status.HTTP_406_NOT_ACCEPTABLE)
                    else:
                        return Response({
                            'message':'username and password required'
                        },status=status.HTTP_406_NOT_ACCEPTABLE)
                else:
                    return Response({'message':'User not found'},status=status.HTTP_404_NOT_FOUND)
            else:
                return Response(data=serializer.errors,status=status.HTTP_406_NOT_ACCEPTABLE)
        except Exception as e:
            print(e)
            return Response({
                'message':'Something went wrong'
            },status=status.HTTP_400_BAD_REQUEST)

""" This API is used to logout """
class LogOutView(APIView):
    def post(self,request):
        try:
            logout(request)
        except Exception as e:
            print(e)

""" This API is used to change password """

class ChangePasswordView(APIView):
    def post(self,request):
        try:
            username=request.GET.get('username')
            data=request.data

            serilizer=ChangePasswordSerializer(data=data)
            if serilizer.is_valid():
                print('sandeep')
                password=serilizer.data['password']
                new_password=serilizer.data['new_password']
                print(new_password)
                if password != new_password:
                    user=Registration.objects.filter(username=username).first()
                    print(user)
                    if user:
                        user.set_password(new_password)
                        user.save()
                        return Response({'message':'Password has been change'},status=status.HTTP_200_OK)
                    else:
                        return Response({
                            'message':'username not found'
                        },status=status.HTTP_404_NOT_FOUND)
                else: 
                    return Response({
                        'message':'Old password and New password same you provide different password'
                    },status=status.HTTP_406_NOT_ACCEPTABLE)
            else:
                return Response(data=serilizer.errors,status=status.HTTP_406_NOT_ACCEPTABLE)
        except Exception as e:
            print(e)
            return Response({'message':'Something went wrong'},status=status.HTTP_400_BAD_REQUEST)

""" This API is used to post data into database """

class PersonalDetailsView(APIView):
    def get(self,request):
        try:
            data=request.GET.get('username')
            if data is not None:
                print(data)
                obj=PersonalDetails.objects.filter(registrations__username=data).first()
                print(obj)
                if obj is not None:
                    serializer=PersonalDetailsSerializer(obj)
                    return Response({'message':serializer.data},status=status.HTTP_200_OK)
                return Response({'message':'Id is not Valid'},status=status.HTTP_404_NOT_FOUND)
            return Response({'message':'Please send id'},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            return Response({'message':'somthing went wrong'},status=status.HTTP_400_BAD_REQUEST)


    def post(self,request):
        try:
            data=request.data
            serializer=PersonalDetailsSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data,status=status.HTTP_200_OK)
            else:
                return Response(data=serializer.errors,status=status.HTTP_406_NOT_ACCEPTABLE)
        except Exception as e:
            print(e)
            return Response({'message':'something went wrong'},status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self,request):
        try:
            username=request.GET.get('username')
            data=request.data
            obj=PersonalDetails.objects.filter(registrations__username=username).first()
            if obj is not None:
                serializer=PersonalDetailsSerializer(obj,data,partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(data=serializer.data,status=status.HTTP_200_OK)
                else:
                    return Response(data=serializer.errors,status=status.HTTP_406_NOT_ACCEPTABLE)
            else:
                return Response({'message':'username not found'},status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print(e)
            return Response({'message':'something went wrong'},status=status.HTTP_400_BAD_REQUEST)

""" This API is used to get all package from database """

class PackageView(APIView):
    def get(self,request):
        try:
            data=Package.objects.all()
            if len(data)>0:
                serializer=PackageSerializer(data,many=True)
                return Response(data=serializer.data,status=status.HTTP_200_OK)
            else:
                return Response(data='no any data',status=status.HTTP_406_NOT_ACCEPTABLE)
        except Exception as e:
            print(e)
            return Response({'message':'something went wrong'},status=status.HTTP_400_BAD_REQUEST)

""" This API is used to get and post data """

class ProjectDetailsView(APIView):

    def get(self,request):
        try:
            username=request.GET.get('username')
            id=request.GET.get('id')
            
            if id:
                obj=ProjectDetails.objects.filter(id=int(id)).first()
                if obj is not None:
                    serializer=SingleProjectSerializer(obj)
                    return Response({'message':serializer.data},status=status.HTTP_200_OK)
                else:
                    return Response({'message':'This Project id is Not there'},status=status.HTTP_404_NOT_FOUND)
            elif username:
                obj=ProjectDetails.objects.filter(registration__username=username)
                if obj:
                    if len(obj) > 0:
                        serializer=ProjectDetailsSerilizer1(obj,many=True)
                        return Response(data=serializer.data,status=status.HTTP_200_OK)
                    else:
                        return Response({'message':'data not available'})
                else:
                    return Response({'message':'username not found'},status=status.HTTP_404_NOT_FOUND)
            
            else:
                obj=ProjectDetails.objects.all()
                if len(obj)>0:
                    serializer=ProjectDetailsSerializer(obj,many=True)
                    return Response({'message':serializer.data},status=status.HTTP_200_OK)
                return Response({'message':'No Any Project Found'},status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print(e)
            return Response({'message':'Something went wrong'},status=status.HTTP_400_BAD_REQUEST)
    
    def post(self,request):
        try:
            data=request.data
            tserializer=TestingProjectDetailsSerializer(data=data)
            if not tserializer.is_valid():
                return Response({'message':tserializer.errors},status=status.HTTP_406_NOT_ACCEPTABLE)
            obj=Registration.objects.filter(id=tserializer.data['id']).first()
            if obj is None:
                return Response({'message':'registration is not valid'},status=status.HTTP_404_NOT_FOUND)
            pserializer=CustomerRegistrationSerializer1(obj)
            return Response(data=pserializer.data,status=status.HTTP_200_OK)
            
        except Exception as e:
            print(e)
            return Response({'message':'something went wrong'},status=status.HTTP_400_BAD_REQUEST)

class TeamView(APIView):
    def get(self,request):
        try:
            user=request.GET.get('username')
            project_id=request.GET.get('project_id')
            if user:
                obj=Team.objects.filter(registration__username=user).first()
                print(obj)
                if obj:
                    serializer=TeamSerializer(obj)
                    return Response(data=serializer.data,status=status.HTTP_200_OK)
                else:
                    return Response({'message':'Team is not there'},status=status.HTTP_404_NOT_FOUND)
            elif project_id:
                obj=Team.objects.filter(project_details__id=int(project_id))
                if len(obj)>0:
                    serializer=TeamSerializer(obj,many=True)
                    return Response(data=serializer.data,status=status.HTTP_200_OK)
                else:
                    return Response(data='No Team Assign there',status=status.HTTP_404_NOT_FOUND)
            else:
                return Response({'message':'username not empty'},status=status.HTTP_406_NOT_ACCEPTABLE)
        except Exception as e:
            print(e)
            return Response({'message':'something went wrong'},status=status.HTTP_400_BAD_REQUEST)

    def patch(self,request):
        try:
            data=request.data
            obj=Team.objects.filter(id=int(data[id])).first()
            if obj is not None:
                serializer=TeamSerializer(obj,data=data,partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(data=serializer.data,status=status.HTTP_200_OK)
                else:
                    return Response(data=serializer.errors,status=status.HTTP_406_NOT_ACCEPTABLE)
            else:
                return Response({'message':'Team Member is not found'},status=status.HTTP_406_NOT_ACCEPTABLE)
        except Exception as e:
            print(e)
            return Response({'message':'something went wrong'},status=status.HTTP_400_BAD_REQUEST)
class VerifyOtp(APIView):
    def post(self,request):
        try:
            email=request.GET.get('email')
            data=request.data
            print(data['otp'])
            obj=Registration.objects.filter(email=email).first()
            print(obj)
            if obj is not None:
                if obj.otp==int(data['otp']):
                    return Response({'message':'Otp veryfied'},status=status.HTTP_200_OK)
                else:
                    return Response({'message':'Otp not match'},status=status.HTTP_406_NOT_ACCEPTABLE)
            else:
                return Response({'message':'Email not found'},status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print(e)
            return Response({'message':'something went wrong'},status=status.HTTP_400_BAD_REQUEST)

class ForgetPassword(APIView):
    def post(self,request):
        try:
            data=request.data
            serializer=EmailValidationSerializer(data=data)
            if not serializer.is_valid():
                return Response(data=serializer.errors,status=status.HTTP_406_NOT_ACCEPTABLE)
            obj=Registration.objects.filter(email=serializer.data['email']).first()
            if obj is None:
                return Response(data='This Email is Register please give valid Register Email',status=status.HTTP_406_NOT_ACCEPTABLE)

            otp=random.randint(999,9999)
            activation_url=f'{otp}'
            confirm=send_otp(obj.email,obj.first_name,activation_url)
            if confirm==True:
                obj.otp=otp
                obj.save()
                return Response({'message':'otp send successfullly'},status=status.HTTP_200_OK)
            return Response({'message':'Try Again'},staus=status.HTTP_406_NOT_ACCEPTABLE)
        except Exception as e:
            print(e)
            return Response({'message':'somthing went wrong'},status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self,request):
        try:
            data=request.data
            serializer=ResetPasswordValidationSerializer(data=data)
            if not serializer.is_valid():
                return Response(data=serializer.errors,status=status.HTTP_406_NOT_ACCEPTABLE)
            if serializer.data['password']!=serializer.data['confirm_password']:
                return Response({'message':'new password and confirm password are not missmatch'},status=status.HTTP_406_NOT_ACCEPTABLE)
            obj=Registration.objects.filter(email=serializer.data['email']).first()
            if obj is None:
                return Response({'message':'Email is not Valid'},status=status.HTTP_406_NOT_ACCEPTABLE)
            set_password_serializer=RegistrationSerializer(obj,data,partial=True)
            if   set_password_serializer.is_valid():
                set_password_serializer.save()
                obj.set_password(serializer.data['password'])
                obj.save()
                return Response({'message':set_password_serializer.data},status=status.HTTP_200_OK)
            else:
                return Response({'message':set_password_serializer.errors},status=status.HTTP_406_NOT_ACCEPTABLE)

        except Exception as e:
            print(e)
            return Response({'message':'somthing went wrong'},status=status.HTTP_400_BAD_REQUEST)
            
