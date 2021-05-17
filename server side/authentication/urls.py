from django.contrib import admin
from django.urls import path, include
from .views import Register, Login, AuthenticateToken


urlpatterns = [
    path('register/', Register.as_view()),
    path('login/', Login.as_view()),
    path('authenticate-token/', AuthenticateToken.as_view())
]
