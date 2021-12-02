from django.shortcuts import render
from accounts.models import ProjectDetails
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from .serializer import *
from rest_framework.views import APIView
from rest_framework import status
# Create your views here.
class InsightView(APIView):
    def post(self,request):
        try:
            data=request.data
            serializer=InsightSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data,status=status.HTTP_200_OK)
            else:
                return Response(data=serializer.errors,status=status.HTTP_406_NOT_ACCEPTABLE)
        except Exception as e:
            print(e)
            return Response({'message':'something went wrong'},status=status.HTTP_400_BAD_REQUEST)
    def get(self,request):
        try:
            # total_project=ProjectDetails.objects.all().count()
            # total_project_value=ProjectDetails.totalValue()
            # total_amount=ProjectDetails.totalAmount()
            obj=Insight.objects.all().first()
            serializer=InsightSerializer(obj)
            return Response({'message':serializer.data},status=status.HTTP_200_OK)

        except Exception as e:
            print(e)
            return Response({'message':'somthing went wrong'},status=status.HTTP_400_BAD_REQUEST)
