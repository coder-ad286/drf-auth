from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from django.core.validators import MinValueValidator, MaxValueValidator,MinLengthValidator,MaxLengthValidator
from django.core.validators import MinLengthValidator


# Create your models here.
class User(AbstractBaseUser):
    name=models.CharField(max_length=20,null=False)
    email = models.EmailField(max_length=20,unique=True,null=False)
    password = models.CharField(max_length=255,null=False)
    age = models.IntegerField(null=False,validators=[MinValueValidator(18)])
    phone=models.BigIntegerField(null=False,default=0)
    is_admin = models.BooleanField(default=False)
    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS =[]
    