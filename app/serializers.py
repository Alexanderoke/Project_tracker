from rest_framework import serializers
from .models import *



class ProjectSerializer(serializers.ModelSerializer):
  class Meta:
    model=Project
    fields='__all__'
    # fields=['project_name','project_type','project_description','project_owner','project_members','github_link']
