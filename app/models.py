from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from cloudinary.models import CloudinaryField


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
