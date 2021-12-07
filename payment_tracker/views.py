from django.shortcuts import render
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
                    obj=PaymentTracker.objects.filter(user__username=username).first()
                    if obj is not None:
                        serializer=PaymentTrackerSerializer(obj)
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
                if username is not None:
                    obj=PaymentInstallment.objects.filter(user__username=username).first()
                    if obj is not None:
                        serializer=PaymentInstallmentSerializer(obj)
                        return Response(data=serializer.data,status=status.HTTP_200_OK)
                    else:
                        return Response({'message':'Username not found'},status=status.HTTP_404_NOT_FOUND)
                else:
                    return Response({'message':'Username is empty'},status=status.HTTP_406_NOT_ACCEPTABLE)       
            except Exception as e:
                print(e)
                return Response({'message':'Something went wrong'},status=status.HTTP_400_BAD_REQUEST)
