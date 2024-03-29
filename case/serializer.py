from rest_framework import serializers
from case.models import Case
from task.models import Task

class CaseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Case
        fields = ('id', 'name', 'task', 'assigned_to')