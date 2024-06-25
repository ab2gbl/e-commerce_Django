from django.db import models
from typing import Iterable, Optional
from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager


class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = 'ADMIN', 'Admin'
        CLIENT = 'CLIENT', 'Client'
    
    base_role=Role.CLIENT 
    role = models.CharField(max_length=50, choices=Role.choices, blank=True)  
    
    def save(self, *args, **kwargs):
        if not self.role:  
            self.role = self.base_role  
        super().save(*args, **kwargs)   
# Create your models here.

class ClientManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        result = super().get_queryset(*args, **kwargs)
        return result.filter(role=User.Role.CLIENT)
        
class Client(User):
    base_role = User.Role.CLIENT
    client = ClientManager()
    class Meta:
        proxy = True
        
        
class AdminManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        result = super().get_queryset(*args, **kwargs)
        return result.filter(role=User.Role.ADMIN)
        
class Admin(User):
    base_role = User.Role.ADMIN
    admin = AdminManager()
    class Meta:
        proxy = True