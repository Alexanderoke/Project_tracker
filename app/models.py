from email.policy import default
from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from cloudinary.models import CloudinaryField
import jsonfield

# Create your models here.
class Manager(BaseUserManager):
  def create_user(self,name, email, password=None):
    if not name:
      raise ValueError("Name is required")
    if not email:
      raise ValueError("Email is required")

    
    user=self.model(
      name=name,
      email=self.normalize_email(email)
    )
    user.set_password(password)
    user.save(using=self._db)
    return user


  def create_superuser(self, name, email, password=None):
    user=self.create_user(
      name=name,
      email=self.normalize_email(email),
      password=password,
    )
    user.is_admin=True
    user.is_staff=True  
    user.is_superuser=True
    user.save(using=self._db)
    return user
    


class NormalUser(AbstractBaseUser):
  name=models.CharField(verbose_name="Name", max_length=50)
  photo=CloudinaryField('image', null=True)
  email=models.EmailField(verbose_name="email address", max_length=50,unique=True)
  date_joined=models.DateTimeField(verbose_name="date joined", auto_now_add=True)
  last_login=models.DateTimeField(verbose_name="last login", auto_now=True)
  is_active=models.BooleanField(default=True)
  is_admin=models.BooleanField(default=True)
  is_staff=models.BooleanField(default=True)
  is_superuser=models.BooleanField(default=False)

  USERNAME_FIELD='email'
  
  REQUIRED_FIELDS=['name']

  objects=Manager()

  def __str__(self):
    return self.name

  def has_perm(self, perm, obj=None):
    return True

  def has_module_perms(self, app_label):
    return True


class Project(models.Model):
  TRACK_SELECTION=(
    ('ANDROID', 'ANDROID'),
    ('FULLSTACK', 'FULLSTACK'),
  )
  project_name=models.CharField(max_length=100)
  project_type=models.CharField(max_length=9, choices=TRACK_SELECTION, default=0)
  project_landingpage=CloudinaryField('image', default='image')
  project_description=models.TextField()
  project_owner=models.CharField(max_length=100)
  project_member1=models.CharField(max_length=50, null=True, blank=True)
  project_member2=models.CharField(max_length=50, null=True, blank=True)
  project_member3=models.CharField(max_length=50, null=True, blank=True)
  project_member4=models.CharField(max_length=50, null=True, blank=True)
  project_member5=models.CharField(max_length=50, null=True, blank=True)
  project_member6=models.CharField(max_length=50, null=True, blank=True)
  github_link=models.URLField(max_length=100)
  # project_members=ArrayField(jsonfield.JSONField(),default=list, null=True)
  # project_members=jsonfield.JSONField()
  # project_members=ArrayField(
  #       ArrayField(
  #           models.CharField(max_length=10, blank=True),
  #           size=8,
  #       ),
  #       size=8,
  #   )

  def __str__(self) -> str:
    return self.project_name