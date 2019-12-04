from django.contrib import admin
from django.urls import path, re_path, include
from apps.tasks import views

urlpatterns = [
    path('list/', views.TasksView.as_view(), name='list_tasks'),
]
