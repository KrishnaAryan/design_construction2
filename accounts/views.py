from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.serializers import Serializer

from .testingSerializer import *
from .serializer import *
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth import authenticate
from django.contrib.auth import logout
# Create your views here.
class RegistrationView(APIView):
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
                            })
                        else:
                            return Response({'message':'Invalid username and password'})
                    else:
                        return Response({
                            'message':'username and password required'
                        })
                else:
                    return Response({'message':'User not found'})
            else:
                return Response({'message':'Invalid data'})
        except Exception as e:
            print(e)
            return Response({
                'message':'Something went wrong'
            })

class LogOutView(APIView):
    def post(self,request):
        try:
            logout(request)
        except Exception as e:
            print(e)


class ChangePasswordView(APIView):
    def post(self,request):
        try:
            username=request.GET.get('username')
            data=request.data
            print(data)
            serilizer=ChangePasswordSerializer(data=data)
            print(serilizer)
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
                        return Response({'message':'Password has been change'})
                    else:
                        return Response({
                            'message':'password not match'
                        })
                else: 
                    return Response({
                        'message':'Old password and New password same you provide different password'
                    })
        except Exception as e:
            print(e)
            return Response({'message':'Something went wrong'})

class PersonalDetailsView(APIView):
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


class ProjectDetailsView(APIView):
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

class TeamSerializerView(APIView):
    def post(self,request):
        try:
            data=request.data
            serializer=TeamSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data,status=status.HTTP_200_OK)
            else:
                return Response(data=serializer.errors,status=status.HTTP_406_NOT_ACCEPTABLE)
        except Exception as e:
            print(e)
            return Response({'message':'something went wrong'},status=status.HTTP_400_BAD_REQUEST)
            

