from django.urls import path
from task.api import TaskListView, TaskDeleteView, TaskCreateView, TaskUpdateView,TaskDetailView

urlpatterns = [
    path('list/', TaskListView.as_view(), name='task_list'),
    path('create/', TaskCreateView.as_view(), name='task_create'),
    path('<int:pk>/update/', TaskUpdateView.as_view(), name='task_update'),
    path('<int:pk>/view/',TaskDetailView.as_view(), name='task_detail'),
    path('<int:pk>/delete/',  TaskDeleteView.as_view(), name='task_delete'),

]