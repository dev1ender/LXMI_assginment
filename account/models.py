from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin ,UserManager
from django.db.models.signals import post_save
from account.service import assign_user_role
from account.utils import ROLES

# Create your models here.


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=150,)
    last_name = models.CharField(max_length=150,blank=True,null=True)
    email = models.EmailField(blank=True, max_length=255, null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    role =models.CharField(max_length=50, choices=ROLES)
    created_on = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey("self",related_name='created_by_user', null=True, blank=True, on_delete=models.SET_NULL)
    updated_by = models.ForeignKey("self", related_name='updated_by_user',on_delete=models.SET_NULL,blank=True, null=True)
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    objects = UserManager()

    class Meta:
        ordering = ['-created_on']

    

def save_account(sender, instance,*args, **kwargs):
    if instance.role:
        assign_user_role(instance)


post_save.connect(save_account,sender=User)





        