from django.contrib import admin
from django.urls import path
from .views import TaskList, TaskCreate


urlpatterns = [
    path('task-list/', TaskList.as_view()),
    path('task-create/', TaskCreate.as_view())
]
