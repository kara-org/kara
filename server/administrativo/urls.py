from django.contrib import admin
from django.urls import path
from .views import *
from rest_framework_jwt.views import obtain_jwt_token
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login/', obtain_jwt_token),
    path('usuarios/', UsuarioView.as_view({'get': 'list', 'post': 'create'}), name='api-usuarios'),
    path('usuario/<int:pk>/', UsuarioDetailView.as_view({'get': 'get', 'put':'put', 'patch': 'patch', 'delete':'delete'}), name='api-usuario'),
    path('usuario/<int:pk_usr>/enderecos/', EnderecoView.as_view({'get': 'list', 'post': 'create'}), name='api-usuario-endereco'),
    path('usuario/<int:pk_usr>/enderecos/<int:pk>/', EnderecoViewDetail.as_view({'get': 'get', 'put':'put', 'patch': 'patch', 'delete':'delete'}), name='api-usuario-endereco'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)