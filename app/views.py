# from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login, logout
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.
class ProjectViewSet(APIView):
  def get(self, request):
    project=Project.objects.all()
    serializer=ProjectSerializer(project, many=True)
    return Response(serializer.data)