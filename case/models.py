from django.db import models
from django.shortcuts import reverse

# Create your models here.
class Case(models.Model):
    name = models.CharField(max_length=200)
    task = models.ManyToManyField('task.Task',blank=True, null=True)
    assigned_to = models.ForeignKey("account.User",null=True, blank=True, on_delete=models.SET_NULL)
    created_on = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey("account.User",related_name='user_create_case', null=True, blank=True, on_delete=models.SET_NULL)
    updated_by = models.ForeignKey("account.User", related_name='user_update_case',on_delete=models.SET_NULL,blank=True, null=True)


    class Meta:
        ordering = ['-created_on']
        default_permissions = ()
        permissions = ( 
            ("case_create", "Can create case"),
            ("case_edit", "Can edit case"), 
            ("case_delete", "Can delete case"), 
            ("case_view", "Can view case"), 
        )
    
    def __str__(self):
        return self.name



