from django.shortcuts import render
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
