from django.db import models
from django.shortcuts import reverse

# Create your models here.
class Case(models.Model):
    name = models.CharField(max_length=200)
    task = models.ManyToManyField('task.Task',blank=True, null=True)
    assigned_to = models.ForeignKey("account.User",null=True, blank=True, on_delete=models.SET_NULL)
    

    class Meta:
        default_permissions = ()
        permissions = ( 
            ("case_create", "Can create case"),
            ("case_edit", "Can edit case"), 
            ("case_delete", "Can delete case"), 
            ("case_view", "Can view case"), 
        )
    
    def __str__(self):
        return self.name



