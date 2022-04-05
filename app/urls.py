from django.urls import path
from .views import *


urlpatterns=[
  path('', project_list),
  path('project/([0-9]+)', project_list),  
]