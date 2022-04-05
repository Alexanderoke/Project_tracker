from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
# from django.contrib.auth import authenticate, login, logout
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http.response import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser


# Create your views here.
# class ProjectViewSet(APIView):
#   def get(self, request):
#     project=Project.objects.all()
#     serializer=ProjectSerializer(project, many=True)
#     return Response(serializer.data)

#   def post(self, request):
#     serializer=ProjectSerializer(data=request.data, many=True)
#     if serializer.is_valid():
#       serializer.save()
#       return JsonResponse(serializer.data, status=201)
#     return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def project_list(request, id=0):
  if request.method=='GET':
    items=Project.objects.all()
    serializer=ProjectSerializer(items, many=True)
    return JsonResponse(serializer.data, safe=False)

  elif request.method=='POST':
    data=JSONParser().parse(request)
    serializer=ProjectSerializer(data=data)
    if serializer.is_valid():
      serializer.save()
      return JsonResponse(serializer.data, status=201, safe=False)
    return JsonResponse(serializer.errors, status=400, safe=False)

  elif request.method=='PUT':
    prodata=JSONParser().parse(request)
    project=Project.objects.get(id=prodata['id'])
    serializer=ProjectSerializer(project, data=prodata)
    if serializer.is_valid():
      serializer.save()
      return JsonResponse(serializer.data, status=201,safe=False)
    return JsonResponse(serializer.errors, status=400, safe=False)

  elif request.method=='DELETE':
    project=Project.objects.get(id=id)
    project.delete()
    return JsonResponse(serializer.errors, status=400, safe=False)