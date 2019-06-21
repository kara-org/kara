from django.contrib import admin
from django.urls import path
from .views import *
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('login/', obtain_jwt_token),
    path('usuarios/', UsuarioView.as_view({'get': 'list'}), name='api-usuarios'),
]