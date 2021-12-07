from django.shortcuts import render

from project_tracker.serializer import ProjecTrackeSerializer
from .models import *
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework import status
# Create your views here.

class ProjectView(APIView):
    def get(self,request):
        try:
            username=request.GET.get('username')
            obj=ProjectTracker.objects.filter(username__username=username)
            if obj:
                serializer=ProjecTrackeSerializer(obj,many=True)
                return Response(data=serializer.data,status=status.HTTP_200_OK)
            else:
                    return Response({'message':'Username not found'},status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print(e)
            return Response({'message':'Something went wrong'},status=status.HTTP_400_BAD_REQUEST)