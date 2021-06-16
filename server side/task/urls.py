from django.contrib import admin
from django.urls import path
from .views import TaskList, TaskCreate, TaskDelete, TaskUpdate, TaskCompleter


urlpatterns = [
    path('task-list/', TaskList.as_view()),
    path('task-create/', TaskCreate.as_view()),
    path('task-delete/<title>/', TaskDelete.as_view()),
    path('task-update/<title>/', TaskUpdate.as_view()),
    path('task-complete/<title>', TaskCompleter.as_view())
]
