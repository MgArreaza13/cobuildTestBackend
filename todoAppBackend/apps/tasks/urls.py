from django.contrib import admin
from django.urls import path, re_path, include
from apps.tasks import views

urlpatterns = [
    path('list/', views.TasksView.as_view(), name='list_tasks'),
    path('new/', views.TaskOptionsView.as_view(), name='new_tasks'),
    path('detail/<int:id_task>/', views.TaskOptionsView.as_view(), name='detail_task'),
    path('edit/<int:id_task>/', views.TaskOptionsView.as_view(), name='update_task'),
    path('delete/<int:id_task>/', views.TaskOptionsView.as_view(), name='delete_task'),
]
