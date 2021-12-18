from django.shortcuts import render
from project_tracker.models import ProjectTracker
from project_tracker.serializer import ProjecTrackeSerializer
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from .serializer import *
from rest_framework.views import APIView
from rest_framework import status

# Create your views here.
class PaymentTrackerView(APIView):
    def get(self,request):
            try:
                username=request.GET.get('username')
                if username is not None:
                    obj=PaymentTracker.objects.filter(user__username=username)
                    if obj is not None:
                        serializer=PaymentTrackerSerializer(obj,many=True)
                        return Response(data=serializer.data,status=status.HTTP_200_OK)
                    else:
                        return Response({'message':'Username not found'},status=status.HTTP_404_NOT_FOUND)
                else:
                    return Response({'message':'Username is empty'},status=status.HTTP_406_NOT_ACCEPTABLE)       
            except Exception as e:
                print(e)
                return Response({'message':'Something went wrong'},status=status.HTTP_400_BAD_REQUEST)


class PaymentInstallmentView(APIView):
    def get(self,request):
            try:
                username=request.GET.get('username')
                project_id = request.GET.get('project_id')
                print("username",username)
                if username:
                    obj=Registration.objects.filter(username=username)
                    print("shiv",obj)
                #return Response({"message":serializer.data},status=status.HTTP_200_OK)
                    if len(obj)>0 :
                        serializer1=PaymetInstallmentSerializer1(obj,many=True)

                        #serializer=PaymentInstallmentSerializer(obj,many=True)
                        return Response(data=serializer1.data,status=status.HTTP_200_OK)
                    else:
                        return Response(data='Username not found',status=status.HTTP_404_NOT_FOUND)
                elif project_id:
                    obj = PaymentInstallment.objects.filter(project__id=project_id)
                    serializer = PaymentInstallmentSerializer(obj,many=True)
                    return Response(data=serializer.data,status=status.HTTP_200_OK)
                else:
                    return Response(data ='Username is empty',status=status.HTTP_406_NOT_ACCEPTABLE)       
            except Exception as e:
                print(e)
                return Response({'message':'Something went wrong'},status=status.HTTP_400_BAD_REQUEST)
