from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render

def returnHome(request):
	return render(request, 'index.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('task.urls')),
    path('api/', include('authentication.urls')),
    path('home/', returnHome)
]
