from django.contrib import admin
from django.urls import path
from .views import *
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('login/', obtain_jwt_token),
    path('auth/usuario/', UsuarioView.as_view({'get': 'retrive'}), name='api-usuarios'),
    path('recuperar-senha/', RecuperarSenhaUsuarioView.as_view({'post': 'create'}), name='api-usuarios'),

    path('usuario/', UsuarioView.as_view({'get': 'list', 'post': 'create'}), name='api-usuarios'),    
    # path('usuario/<int:pk>/', UsuarioDetailView.as_view({'get': 'get', 'put':'put', 'patch': 'patch', 'delete':'delete'}), name='api-usuario'),
    # path('usuario/<int:pk_usr>/enderecos/', EnderecoView.as_view({'get': 'list', 'post': 'create'}), name='api-usuario-endereco'),
    #path('usuario/<int:pk_usr>/enderecos/<int:pk>/', EnderecoViewDetail.as_view({'get': 'get', 'put':'put', 'patch': 'patch', 'delete':'delete'}), name='api-usuario-endereco'),
    path('usuario/<int:pk_usr>/telefones/', TelefoneView.as_view({'get': 'list', 'post': 'create'}), name='api-usuario-telefone'),
    path('usuario/<int:pk_usr>/telefones/<int:pk>/', TelefoneViewDetail.as_view({'get': 'get', 'put':'put', 'patch': 'patch', 'delete':'delete'}), name='api-usuario-telefone'),
    
    path('ong/', ONGView.as_view({'get': 'list', 'post': 'create'}), name='ongs'),
    path('usuarios/', UsuarioView.as_view({'get': 'list', 'post': 'create'}), name='api-usuarios'),
    path('usuario/<int:pk>/', UsuarioDetailView.as_view({'get': 'get', 'put':'put', 'patch': 'patch', 'delete':'delete'}), name='api-usuario'),
    path('ong/', OngCreateView.as_view({'post': 'create'}), name='ongs'),
    path('ongs/', ONGListView.as_view({'get': 'list'}), name='ongs'),
    path('ong/<int:pk>/', OngDetailView.as_view({'get': 'get', 'put':'put', 'patch': 'patch', 'delete':'delete'}), name='ong'),

]

# busca_patterns = [
#     path('busca/', BuscaView.as_view({ 'post': 'create'}), name='busca') #sem jwt

# ]

# ong_pattern = [
#     path('ong/', OngView.as_view({'get': 'list', 'post': 'create'}), name='ongs'),
#     path('ong/<int:pk>/', OngDetailView.as_view({'get': 'get', 'put':'put', 'patch': 'patch', 'delete':'delete'}), name='ong'),
#     path('ong/<int:pk>/doacoes/', OngPerfilView.as_view({'get': 'list', 'post': 'create'}), name='ong-perfil'),
#     path('ong/<int:pk>/doacoes/<int:id_doacao>/', GerirDoacoesView.as_view({'get': 'get', 'put':'put', 'patch': 'patch', 'delete':'delete'}), name='gerir-ong-perfil'),
#     path('ong/<int:pk>/doacoes/', DemandaView.as_view({'get': 'list', 'post': 'create'}), name='ong-demanda'),
#     path('ong/<int:pk>/doacoes/<int:id_doacao>/', DemandaView.as_view({'get': 'get', 'put':'put', 'patch': 'patch', 'delete':'delete'}), name='gerir-ong-demanda')
# ]

# doador_pattern = [
#     path('doador/', DoadorView.as_view({'get': 'list', 'post': 'create'}), name='doadores'),
#     path('doador/<int:pk>/', DoadorDetailView.as_view({'get': 'get', 'put':'put', 'patch': 'patch', 'delete':'delete'}), name='doador'),
#     path('doador/<int:pk>/doacoes/', OngPerfilView.as_view({'get': 'list', 'post': 'create'}), name='ong-perfil'),
#     path('doador/<int:pk>/doacoes/<int:id_doacao>/', GerirDoacoesView.as_view({'get': 'get', 'put':'put', 'patch': 'patch', 'delete':'delete'}), name='gerir-ong-perfil')
# ]




# urlpatterns = [usuario_anterior]
# urlpatterns += [busca_patterns, ong_pattern, doador_pattern ]

