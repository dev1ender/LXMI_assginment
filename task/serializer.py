from rest_framework import serializers
from task.models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'name', 'content', 'created_on', 'created_by','updated_on','updated_by')