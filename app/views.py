# from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login, logout
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser


# Create your views here.
class ProjectViewSet(APIView):
  def get(self, request):
    project=Project.objects.all()
    serializer=ProjectSerializer(project, many=True)
    return Response(serializer.data)
  def detail(request, pk):
    try:
      pro=Project.objects.get(pk=pk)
    except Project.DoesNotExist:
      return HttpResponse(status=404)
  # def project_list(request):
  #   if request.method=='GET':
  #     items=Project.objects.all()
  #     serializer=ProjectSerializer(items, many=True)
  #     return JsonResponse(serializer.data)

  #   elif request.method=='POST':
  #     data=JSONParser().parse(request)
  #     serializer=ProjectSerializer(data=data)
  #     if serializer.is_valid():
  #       serializer.save()
  #       return JsonResponse(serializer.data, status=201)
  #     return JsonResponse(serializer.errors, status=400)