from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from .serializer import *
from rest_framework.views import APIView
from rest_framework import status
from accounts.models import *
from django.core.cache import cache
# Create your views here.
class AgreementsView(APIView):
    def get(self,request):
            try:
                username=request.GET.get('username')
                if cache.get(username):
                    print('data from cache')
                    agreement=cache.get(username)
                    return JsonResponse(agreement,safe=False)
                else:
                    if username is not None:
                        project=ProjectDetails.objects.filter(registration__username=username).first()
                        print(project)
                        if project is not None:
                            obj=Agreements.objects.filter(project_details__id=project.id)
                            if len(obj)>0:
                                serializer=AgreementsSerializer(obj,many=True,context={'request': request})
                                cache.set(username,serializer.data)
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
                id =request.GET.get('id')
                if cache.get(username):
                    print('data from cache')
                    document=cache.get(username)
                    return JsonResponse(document,safe=False)
                elif cache.get(id):
                    print('data from cache using id')
                    document=cache.get(id)
                    return JsonResponse(document,safe=False)
                else:
                    if username is not None:
                        project=ProjectDetails.objects.filter(registration__username=username).first()
                        print(project)
                        if project is not None:
                            obj=Documents.objects.filter(project_details__id=project.id)
                            if len(obj)>0:
                                serializer=DocumentsSerializer(obj,many=True,context={'request': request})
                                cache.set(username,serializer.data)
                                return Response(data=serializer.data,status=status.HTTP_200_OK)
                            else:
                                return Response({'message':'Id not found'},status=status.HTTP_404_NOT_FOUND)
                        else:
                            return Response({'message':'No Any  Document Found'},status=status.HTTP_404_NOT_FOUND)
                    elif id is not None:
                        obj=Documents.objects.filter(id=id)
                        serializer=DocumentsSerializer(obj,many=True,context={'request': request})
                        cache.set(id,serializer.data)
                        return Response(data=serializer.data,status=status.HTTP_200_OK)
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
                if cache.get(username):
                    print('data from cache')
                    concept=cache.get(username)
                    return JsonResponse(concept,safe=False)
                else:
                    if username is not None:
                        project=ProjectDetails.objects.filter(registration__username=username).first()
                        print(project)
                        if project is not None:
                            obj=ConceptPlans.objects.filter(project_details__id=project.id)
                            if len(obj)>0:
                                serializer=ConceptPlansSerializer(obj,many=True,context={'request': request})
                                cache.set(username,serializer.data)
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
                if cache.get(username):
                    print('data from cache')
                    working=cache.get(username)
                    return JsonResponse(working,safe=False)
                else:
                    if username is not None:
                        project=ProjectDetails.objects.filter(registration__username=username).first()
                        print(project)
                        if project is not None:
                            obj=WorkingDrawings.objects.filter(project_details__id=project.id)
                            if len(obj)>0:
                                serializer=WorkingDrawingsSerializer(obj,many=True,context={'request': request})
                                cache.set(username,serializer.data)
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
                if cache.get(username):
                    print('get data from cache')
                    structural=cache.get(username)
                    return JsonResponse(structural,safe=False)
                if username is not None:
                    project=ProjectDetails.objects.filter(registration__username=username).first()
                    print(project)
                    if project is not None:
                        obj=StructuralDrawings.objects.filter(project_details__id=project.id)
                        if len(obj)>0:
                            serializer=StructuralDrawingsSerializer(obj,many=True,context={'request': request})
                            cache.set(username,serializer.data)
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

class ThreeDView(APIView):
    def get(self,request):
            try:
                username=request.GET.get('username')
                if cache.get(username):
                    print('get data from cache')
                    three_d=cache.get(username)
                    return JsonResponse(three_d,safe=False)
                if username is not None:
                    project=ProjectDetails.objects.filter(registration__username=username).first()
                    print(project)
                    if project is not None:
                        obj=ThreeDModel.objects.filter(project_details__id=project.id).first()
                        if obj is not None:
                            serializer=ThreeDSerializer(obj,context={'request':request})
                            cache.set(username,serializer.data)
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

class GalleryImageView(APIView):
    def get(self,request):
        try:
            user=request.GET.get('username')
            if cache.get(user):
                print('get data from cache')
                gallery=cache.get(user)
                return JsonResponse(gallery,safe=False)
            # p=InsideImage.objects.filter(gallery_image__user_name__username=user)
            # print(p)
            obj=GalleryImage.objects.filter(user_name__username=user)
            if len(obj)>0:
                serializer=GalleryImageSerializer(obj,many=True,context={'request': request})
                cache.set(user,serializer.data)
                return Response(data=serializer.data,status=status.HTTP_200_OK)
            else:
                return Response({'message':'Username not found'},status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print(e)
            return Response({'message':'Something went wrong'},status=status.HTTP_400_BAD_REQUEST)
