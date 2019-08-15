from django.contrib import admin
from django.urls import path
from administrativo.views import *
from doacoes.views import *
from campanhas.views import *
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('login/', obtain_jwt_token),
    path('auth/usuario/', UsuarioView.as_view({'get': 'retrive'}), name='api-usuarios'),
    path('recuperar-senha/', RecuperarSenhaUsuarioView.as_view({'post': 'create'}), name='api-usuarios'),

    path('usuario/', UsuarioView.as_view({'get': 'list', 'post': 'create'}), name='api-usuarios'),
    path('usuario/<int:pk>/', UsuarioDetailView.as_view({'get': 'get', 'put': 'put', 'patch': 'patch',
                                                         'delete': 'delete'}), name='api-usuario'),
    path('usuario/<int:pk_usr>/telefones/', TelefoneView.as_view({'get': 'list', 'post': 'create'}),
         name= 'api-usuario-telefone'),
    path('usuario/<int:pk_usr>/telefones/<int:pk>/', TelefoneViewDetail.as_view({'get': 'get', 'put': 'put',
                                                                                 'patch': 'patch', 'delete': 'delete'}),
         name='api-usuario-telefone'),

    path('ong/', OngCreateListView.as_view({'get': 'list', 'post': 'create'}), name='ongs'),
    path('ong/<int:pk>/', OngDetailView.as_view({'get': 'get', 'put': 'put', 'patch': 'patch',
                                                 'delete': 'delete'}), name='ong'),
    path('ong/<int:id_ong>/demandas/', DemandaView.as_view({'get': 'list', 'post': 'create'}), name='demanda'),

    path('demanda/<int:pk>/', DemandaView.as_view({'put': 'put', 'patch': 'patch'}), name='alterar_demanda'),
    path('demanda/<int:pk>/cancelar', DemandaView.as_view({'delete': 'delete'}), name='cancelar_demanda'),
    path('demandas/', DemandaListView.as_view({'get': 'list'}), name='demandas'),

    path('doacao/', DoacaoView.as_view({'post': 'create'}), name='doacao'),
]
