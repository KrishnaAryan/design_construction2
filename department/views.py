from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from .serializer import *
from rest_framework.views import APIView
from rest_framework import status
# Create your views here.
class FinanceView(APIView):
    def get(self,request):
        try:
            id=request.GET.get('id')
            if id is not None:
                obj=Finance.objects.filter(emp_id=id).first()
                if obj is not None:
                    print(obj)
                    serializer=FinanceSerializer(obj)
                    return Response(data=serializer.data,status=status.HTTP_200_OK)
                else:
                    return Response({'message':'Id not found'},status=status.HTTP_404_NOT_FOUND)
            else:
                return Response({'message':'Id is empty'},status=status.HTTP_406_NOT_ACCEPTABLE)       
        except Exception as e:
            print(e)
            return Response({'message':'Something went wrong'},status=status.HTTP_400_BAD_REQUEST)

    def post(self,request):
        try:
            data=request.data
            serializer=FinanceSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data,status=status.HTTP_200_OK)
            else:
                return Response(data=serializer.errors,status=status.HTTP_406_NOT_ACCEPTABLE)
        except Exception as e:
            print(e)
            return Response({'message':'something went wrong'},status=status.HTTP_400_BAD_REQUEST)
class ProjectCoordinationView(APIView):
    def get(self,request):
        try:
            id=request.GET.get('id')
            if id is not None:
                obj=ProjectCoordination.objects.filter(emp_id=id).first()
                if obj is not None:
                    serializer=ProjectCoordinationSerializer(obj)
                    return Response(data=serializer.data,status=status.HTTP_200_OK)
                else:
                    return Response({'message':'Id not found'},status=status.HTTP_404_NOT_FOUND)
            else:
                return Response({'message':'Id is empty'},status=status.HTTP_406_NOT_ACCEPTABLE)       
        except Exception as e:
            print(e)
            return Response({'message':'Something went wrong'},status=status.HTTP_400_BAD_REQUEST)

    def post(self,request):
        try:
            data=request.data
            serializer=ProjectCoordinationSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data,status=status.HTTP_200_OK)
            else:
                return Response(data=serializer.errors,status=status.HTTP_406_NOT_ACCEPTABLE)
        except Exception as e:
            print(e)
            return Response({'message':'something went wrong'},status=status.HTTP_400_BAD_REQUEST)

class DesignTeamView(APIView):
    def get(self,request):
            try:
                username=request.GET.get('username')
                if username is not None:
                    project=ProjectDetails.objects.filter(registration__username=username).first()
                    print(project.id)
                    obj=DesignTeam.objects.filter(project_details__id=project.id).first()
                    if obj is not None:
                        print(obj)
                        serializer=DesignTeamSerializer(obj)
                        return Response(data=serializer.data,status=status.HTTP_200_OK)
                    else:
                        return Response({'message':'username not found'},status=status.HTTP_404_NOT_FOUND)
                else:
                    return Response({'message':'Username is empty'},status=status.HTTP_406_NOT_ACCEPTABLE)       
            except Exception as e:
                print(e)
                return Response({'message':'Something went wrong'},status=status.HTTP_400_BAD_REQUEST)

    def post(self,request):
        try:
            data=request.data
            serializer=DesignTeamSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data,status=status.HTTP_200_OK)
            else:
                return Response(data=serializer.errors,status=status.HTTP_406_NOT_ACCEPTABLE)
        except Exception as e:
            print(e)
            return Response({'message':'something went wrong'},status=status.HTTP_400_BAD_REQUEST)
class ExecutionTeamView(APIView):
    def get(self,request):
            try:
                id=request.GET.get('id')
                if id is not None:
                    obj=ExecutionTeam.objects.filter(emp_id=id).first()
                    if obj is not None:
                        serializer=ExecutionTeamSerializer(obj)
                        return Response(data=serializer.data,status=status.HTTP_200_OK)
                    else:
                        return Response({'message':'Id not found'},status=status.HTTP_404_NOT_FOUND)
                else:
                    return Response({'message':'Id is empty'},status=status.HTTP_406_NOT_ACCEPTABLE)       
            except Exception as e:
                print(e)
                return Response({'message':'Something went wrong'},status=status.HTTP_400_BAD_REQUEST)

    def post(self,request):
        try:
            data=request.data
            serializer=ExecutionTeamSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data,status=status.HTTP_200_OK)
            else:
                return Response(data=serializer.errors,status=status.HTTP_406_NOT_ACCEPTABLE)
        except Exception as e:
            print(e)
            return Response({'message':'something went wrong'},status=status.HTTP_400_BAD_REQUEST)
