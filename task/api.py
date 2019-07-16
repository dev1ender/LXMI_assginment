from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.http import Http404
from task.models import Task
from task.serializer import TaskSerializer
from account.utils import access_permission
from account.db import get_all_objects
from account.db import get_object

class TaskListView(APIView):
    permission_classes = (IsAuthenticated,)
    model = Task

    @access_permission('task_view')
    def get(self, request, format=None):
        task = get_all_objects(self)
        serializer = TaskSerializer(task, many=True)
        return Response(serializer.data)
    
class TaskCreateView(APIView):
    permission_classes = (IsAuthenticated,)

    @access_permission('task_create')
    def post(self, request, format=None):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TaskUpdateView(APIView):
    permission_classes = (IsAuthenticated,)
    model = Task

    @access_permission('task_edit')
    def post(self, request,pk, format=None):
        task = get_object(self,pk)
        serializer = TaskSerializer(task,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskDeleteView(APIView):
    permission_classes = (IsAuthenticated,)
    model = Task

    @access_permission('task_delete')
    def delete(self, request, pk, format=None):
        task = get_object(self,pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TaskDetailView(APIView):
    permission_classes = (IsAuthenticated,)
    model = Task

    @access_permission('task_view')
    def get(self, request,pk, format=None):
        task = get_object(self,pk)
        serializer = TaskSerializer(task)
        return Response(serializer.data)



