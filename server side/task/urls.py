from django.contrib import admin
from django.urls import path
from .views import TaskList, TaskCreate, TaskDelete, TaskUpdate


urlpatterns = [
    path('task-list/', TaskList.as_view()),
    path('task-create/', TaskCreate.as_view()),
    path('task-delete/<id>/', TaskDelete.as_view()),
    path('task-update/<id>/', TaskUpdate.as_view())
]
