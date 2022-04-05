from email.policy import default
from rest_framework import serializers
from .models import *



class ProjectSerializer(serializers.ModelSerializer):
  # project_name=serializers.SlugRelatedField(many=True, slug_field='project_name', queryset=Project.objects.all())
  class Meta:
    model=Project
    fields='__all__'
    # fields=['project_name','project_type','project_description','project_owner','project_members','github_link']
    # id=serializers.IntegerField(read_only=True)
    # project_name=serializers.CharField(required=True, allow_blank=False, max_length=100)
    # project_type=serializers.ChoiceField(choices='TRACK_SELECTION', default='FULLSTACK')
    # project_description=serializers.CharField(required=True, allow_blank=False, max_length=150)
    # project_owner=serializers.CharField(required=True, allow_blank=False, max_length=50)
    # project_member1=serializers.CharField(required=False, allow_blank=True, max_length=50)
    # project_member2=serializers.CharField(required=False, allow_blank=True, max_length=50)
    # project_member3=serializers.CharField(required=False, allow_blank=True, max_length=50)
    # project_member4=serializers.CharField(required=False, allow_blank=True, max_length=50)
    # project_member5=serializers.CharField(required=False, allow_blank=True, max_length=50)
    # project_member6=serializers.CharField(required=False, allow_blank=True, max_length=50)
    # github_link=serializers.URLField(required=True,allow_blank=False)


  def create(self, validated_data):
    return Project.objects.create(**validated_data)

  
  def update(self, instance, validated_data):
    instance.project_name=validated_data.get('project_name', instance.project_name)
    instance.project_type=validated_data.get('project_type', instance.project_type)
    instance.project_description=validated_data.get('project_description', instance.project_description)
    instance.project_owner=validated_data.get('project_owner', instance.project_owner)
    instance.project_member1=validated_data.get('project_member1', instance.project_member1)
    instance.project_member2=validated_data.get('project_member2', instance.project_member2)
    instance.project_member3=validated_data.get('project_member3', instance.project_member3)
    instance.project_member4=validated_data.get('project_member4', instance.project_member4)
    instance.project_member5=validated_data.get('project_member5', instance.project_member5)
    instance.project_member6=validated_data.get('project_member6', instance.project_member6)
    instance.github_link=validated_data.get('github_link', instance.github_link)
    instance.save()
    return instance