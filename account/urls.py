from django.urls import path
from account.api import UserListView, UserDeleteView, UserCreateView, UserUpdateView,UserDetailView

urlpatterns = [
    path('list/', UserListView.as_view(), name='user_list'),
    path('create/', UserCreateView.as_view(), name='user_create'),
    path('<int:pk>/update/', UserUpdateView.as_view(), name='user_update'),
    path('<int:pk>/view/', UserDetailView.as_view(), name='user_detail'),
    path('<int:pk>/delete/', UserDeleteView.as_view(), name='user_delete'),

]
