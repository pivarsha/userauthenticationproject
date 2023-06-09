from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=True, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)   
    mobile = models.CharField(max_length=10,blank = True,null=None)  
    first_name = models.CharField(max_length=30)  
    last_name = models.CharField(max_length=30) 
    is_active = models.BooleanField(default=True) 
    is_staff = models.BooleanField(default=False)   
    date_joined = models.DateTimeField(auto_now_add=True)   

    USERNAME_FIELD = 'email'    
    REQUIRED_FIELDS = ['first_name', 'last_name','mobile']      

    objects = CustomUserManager() 

    def __str__(self):
        return self.email