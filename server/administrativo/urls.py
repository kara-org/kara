from django.contrib import admin
from django.urls import path
from .views import *
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('login/', obtain_jwt_token),
    path('auth/usuario/', UsuarioView.as_view({'get': 'retrive'}), name='api-usuarios'),
    path('auth/u/', UView.as_view({'get': 'list'}), name='api-usuarios'),
    path('recuperar-senha/', UView.as_view({'post': 'create'}), name='api-usuarios'),
]