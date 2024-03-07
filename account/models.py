from django.db import models
from django.contrib.auth.models import AbstractUser
from .custommanagers import CustomUserManager
from .choices import ROLE
# Create your models here.


class CustomUser(AbstractUser):
    email = models.EmailField(max_length=320,unique=True)
    phone_number = models.CharField(max_length=15,unique=True)
    role = models.PositiveIntegerField(choices=ROLE,null=False)
    full_name = models.CharField(max_length=64,null=False)
    username=None
    created_date= models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS=['full_name','phone_number','role']

    objects = CustomUserManager()

    def get_role(self):
        if self.role== 1:
            return 'Superadmin'
        elif self.role == 2:
            return 'Admin'
        else:
            return 'User'
    

