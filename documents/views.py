from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from .serializer import *
from rest_framework.views import APIView
from rest_framework import status
from accounts.models import *
# Create your views here.
class AgreementsView(APIView):
    def get(self,request):
            try:
                username=request.GET.get('username')
                if username is not None:
                    project=ProjectDetails.objects.filter(registration__username=username).first()
                    print(project)
                    if project is not None:
                        obj=Agreements.objects.filter(project_details__id=project.id).first()
                        if obj is not None:
                            serializer=AgreementsSerializer(obj)
                            return Response(data=serializer.data,status=status.HTTP_200_OK)
                        else:
                            return Response({'message':'Id not found'},status=status.HTTP_404_NOT_FOUND)
                    else:
                        return Response({'message':'No Any Agreement Document Found'},status=status.HTTP_404_NOT_FOUND)
                else:
                    return Response({'message':'Id is empty'},status=status.HTTP_406_NOT_ACCEPTABLE)       
            except Exception as e:
                print(e)
                return Response({'message':'Something went wrong'},status=status.HTTP_400_BAD_REQUEST)

    # def post(self,request):
    #     try:
    #         data=request.data
    #         serializer=AgreementsSerializer(data=data)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return Response(data=serializer.data,status=status.HTTP_200_OK)
    #         else:
    #             return Response(data=serializer.errors,status=status.HTTP_406_NOT_ACCEPTABLE)
    #     except Exception as e:
    #         print(e)
    #         return Response({'message':'something went wrong'},status=status.HTTP_400_BAD_REQUEST)

class DocumentsView(APIView):
    def get(self,request):
            try:
                username=request.GET.get('username')
                if username is not None:
                    project=ProjectDetails.objects.filter(registration__username=username).first()
                    print(project)
                    if project is not None:
                        obj=Documents.objects.filter(project_details__id=project.id).first()
                        if obj is not None:
                            serializer=DocumentsSerializer(obj)
                            return Response(data=serializer.data,status=status.HTTP_200_OK)
                        else:
                            return Response({'message':'Id not found'},status=status.HTTP_404_NOT_FOUND)
                    else:
                        return Response({'message':'No Any  Document Found'},status=status.HTTP_404_NOT_FOUND)
                else:
                    return Response({'message':'Id is empty'},status=status.HTTP_406_NOT_ACCEPTABLE)       
            except Exception as e:
                print(e)
                return Response({'message':'Something went wrong'},status=status.HTTP_400_BAD_REQUEST)

    # def post(self,request):
    #     try:
    #         data=request.data
    #         serializer=DocumentsSerializer(data=data)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return Response(data=serializer.data,status=status.HTTP_200_OK)
    #         else:
    #             return Response(data=serializer.errors,status=status.HTTP_406_NOT_ACCEPTABLE)
    #     except Exception as e:
    #         print(e)
    #         return Response({'message':'something went wrong'},status=status.HTTP_400_BAD_REQUEST)

class ConceptPlansView(APIView):
    def get(self,request):
            try:
                username=request.GET.get('username')
                if username is not None:
                    project=ProjectDetails.objects.filter(registration__username=username).first()
                    print(project)
                    if project is not None:
                        obj=ConceptPlans.objects.filter(project_details__id=project.id).first()
                        if obj is not None:
                            serializer=ConceptPlansSerializer(obj)
                            return Response(data=serializer.data,status=status.HTTP_200_OK)
                        else:
                            return Response({'message':'Id not found'},status=status.HTTP_404_NOT_FOUND)
                    else:
                        return Response({'message':'No Any ConceptPlans Document Found'},status=status.HTTP_404_NOT_FOUND)
                else:
                    return Response({'message':'Id is empty'},status=status.HTTP_406_NOT_ACCEPTABLE)       
            except Exception as e:
                print(e)
                return Response({'message':'Something went wrong'},status=status.HTTP_400_BAD_REQUEST)

    # def post(self,request):
    #     try:
    #         data=request.data
    #         serializer=ConceptPlansSerializer(data=data)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return Response(data=serializer.data,status=status.HTTP_200_OK)
    #         else:
    #             return Response(data=serializer.errors,status=status.HTTP_406_NOT_ACCEPTABLE)
    #     except Exception as e:
    #         print(e)
    #         return Response({'message':'something went wrong'},status=status.HTTP_400_BAD_REQUEST)


class WorkingDrawingsView(APIView):
    def get(self,request):
            try:
                username=request.GET.get('username')
                if username is not None:
                    project=ProjectDetails.objects.filter(registration__username=username).first()
                    print(project)
                    if project is not None:
                        obj=WorkingDrawings.objects.filter(project_details__id=project.id).first()
                        if obj is not None:
                            serializer=WorkingDrawingsSerializer(obj)
                            return Response(data=serializer.data,status=status.HTTP_200_OK)
                        else:
                            return Response({'message':'Id not found'},status=status.HTTP_404_NOT_FOUND)
                    else:
                        return Response({'message':'No Any working drawings Document Found'},status=status.HTTP_404_NOT_FOUND)
                else:
                    return Response({'message':'Id is empty'},status=status.HTTP_406_NOT_ACCEPTABLE)       
            except Exception as e:
                print(e)
                return Response({'message':'Something went wrong'},status=status.HTTP_400_BAD_REQUEST)

    # def post(self,request):
    #     try:
    #         data=request.data
    #         serializer=WorkingDrawingsSerializer(data=data)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return Response(data=serializer.data,status=status.HTTP_200_OK)
    #         else:
    #             return Response(data=serializer.errors,status=status.HTTP_406_NOT_ACCEPTABLE)
    #     except Exception as e:
    #         print(e)
    #         return Response({'message':'something went wrong'},status=status.HTTP_400_BAD_REQUEST)


class StructuralDrawingsView(APIView):
    
    def get(self,request):
            try:
                username=request.GET.get('username')
                if username is not None:
                    project=ProjectDetails.objects.filter(registration__username=username).first()
                    print(project)
                    if project is not None:
                        obj=StructuralDrawings.objects.filter(project_details__id=project.id).first()
                        if obj is not None:
                            serializer=StructuralDrawingsSerializer(obj)
                            return Response(data=serializer.data,status=status.HTTP_200_OK)
                        else:
                            return Response({'message':'Id not found'},status=status.HTTP_404_NOT_FOUND)
                    else:
                        return Response({'message':'No Any structural drawings Document Found'},status=status.HTTP_404_NOT_FOUND)
                else:
                    return Response({'message':'Id is empty'},status=status.HTTP_406_NOT_ACCEPTABLE)       
            except Exception as e:
                print(e)
                return Response({'message':'Something went wrong'},status=status.HTTP_400_BAD_REQUEST)

    # def post(self,request):
    #     try:
    #         data=request.data
    #         serializer=StructuralDrawingsSerializer(data=data)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return Response(data=serializer.data,status=status.HTTP_200_OK)
    #         else:
    #             return Response(data=serializer.errors,status=status.HTTP_406_NOT_ACCEPTABLE)
    #     except Exception as e:
    #         print(e)
    #         return Response({'message':'something went wrong'},status=status.HTTP_400_BAD_REQUEST)

class ThreeDSerializerView(APIView):
    def get(self,request):
            try:
                username=request.GET.get('username')
                if username is not None:
                    project=ProjectDetails.objects.filter(registration__username=username).first()
                    print(project)
                    if project is not None:
                        obj=ThreeD.objects.filter(project_details__id=project.id).first()
                        if obj is not None:
                            serializer=ThreeDSerializer(obj)
                            return Response(data=serializer.data,status=status.HTTP_200_OK)
                        else:
                            return Response({'message':'Id not found'},status=status.HTTP_404_NOT_FOUND)
                    else:
                        return Response({'message':'No Any structural drawings Document Found'},status=status.HTTP_404_NOT_FOUND)
                else:
                    return Response({'message':'Id is empty'},status=status.HTTP_406_NOT_ACCEPTABLE)       
            except Exception as e:
                print(e)
                return Response({'message':'Something went wrong'},status=status.HTTP_400_BAD_REQUEST)


    # def post(self,request):
    #     try:
    #         data=request.data
    #         serializer=ThreeDSerializer(data=data)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return Response(data=serializer.data,status=status.HTTP_200_OK)
    #         else:
    #             return Response(data=serializer.errors,status=status.HTTP_406_NOT_ACCEPTABLE)
    #     except Exception as e:
    #         print(e)
    #         return Response({'message':'something went wrong'},status=status.HTTP_400_BAD_REQUEST)

