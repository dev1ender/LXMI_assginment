from django.db import models
from django.shortcuts import reverse

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=200,blank=True)
    content = models.CharField(max_length=200, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey("account.User",related_name='user_create_task', null=True, blank=True, on_delete=models.SET_NULL)
    updated_by = models.ForeignKey("account.User", related_name='user_update_task',on_delete=models.SET_NULL,blank=True, null=True)

    
    class Meta:
        ordering = ['-created_on']
        default_permissions = ()
        permissions = ( 
            ("task_create", "Can create task"),
            ("task_edit", "Can edit task"), 
            ("task_delete", "Can delete task"), 
            ("task_view", "Can view task"), 
        )

    def __str__(self):
        return self.name

