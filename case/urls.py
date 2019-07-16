from django.urls import path
from case.api import CaseListView, CaseDeleteView, CaseCreateView, CaseUpdateView,CaseDetailView

urlpatterns = [
    path('list/', CaseListView.as_view(), name='case_list'),
    path('create/', CaseCreateView.as_view(), name='case_create'),
    path('<int:pk>/update/', CaseUpdateView.as_view(), name='case_update'),
    path('<int:pk>/view/', CaseDetailView.as_view(), name='case_detail'),
    path('<int:pk>/delete/', CaseDeleteView.as_view(), name='case_delete'),

]
