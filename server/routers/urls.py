from django.contrib import admin
from django.urls import path
from administrativo.views import *
from doacoes.views import *
from campanhas.views import *
from rest_framework_jwt.views import obtain_jwt_token

autenticacao_patterns = [
     path('login/', obtain_jwt_token),
     path('auth/usuario/', UsuarioView.as_view({'get': 'retrive'}), name='api-usuarios'),
     path('recuperar-senha/', RecuperarSenhaUsuarioView.as_view({'post': 'create'}), name='api-usuarios'),
]

usuario_patterns = [
     path('usuario/', UsuarioView.as_view({'get': 'list', 'post': 'create'}), name='api-usuarios'),
     path('usuario/<int:pk>/', UsuarioDetailView.as_view({'get': 'get', 'put': 'put', 'patch': 'patch',
                                                       'delete': 'delete'}), name='api-usuario'),
     path('usuario/<int:pk_usr>/telefones/', TelefoneView.as_view({'get': 'list', 'post': 'create'})
                                                                 ,name= 'api-usuario-telefone'),
     path('usuario/<int:pk_usr>/telefones/<int:pk>/', TelefoneViewDetail.as_view({'get': 'get', 'put': 'put',
                                                                                 'patch': 'patch', 'delete': 'delete'})
                                                                                  ,name='api-usuario-telefone'),
]

ong_patterns = [
    path('ong/', OngCreateListView.as_view({'get': 'list', 'post': 'create'}), name='ongs'),
    path('ong/<int:pk>/', OngDetailView.as_view({'get': 'get', 'put': 'put', 'patch': 'patch',
                                                 'delete': 'delete'}), name='ong'),
    path('ong/<int:id_ong>/demandas/', DemandaView.as_view({'get': 'list', 'post': 'create'}), name='demanda'),  
]

demanda_patterns = [
    path('demanda/<int:pk>/', DemandaView.as_view({'put': 'put', 'patch': 'patch'}), name='alterar_demanda'),
    path('demanda/<int:pk>/cancelar', DemandaView.as_view({'delete': 'delete'}), name='cancelar_demanda'),
    path('demandas/', DemandaListView.as_view({'get': 'list'}), name='demandas'),
]

doacao_patterns = [
    path('doacao/', DoacaoView.as_view({'post': 'create'}), name='doacao'),
    path('ong/<int:id_ong>/doacoes/', DoacaoView.as_view({'get': 'list'}), name='lista_doacao'),
    path('doador/<int:id_user>/doacoes/', DoacaoViewUser.as_view({'get': 'list'}), name='lista_doacao_user'),
    path('doacao/<int:pk>/confirmar/', DoacaoViewUser.as_view({'post': 'post'}), name='confirmar_doacao'),
    path('doacao/<int:pk>/cancelar/', DoacaoViewUser.as_view({'delete': 'destroy'}), name='cancelar_doacao')
]

item_doacao =[
    path('item/<int:pk>/confirmar/', ItemDoacaoView.as_view({'post': 'post'}), name='confirmar_item_doacao'),
    path('item/<int:pk>/cancelar/', ItemDoacaoView.as_view({'delete': 'delete'}), name='cancelar_item_doacao'),
    path('item/<int:pk>/', ItemDoacaoView.as_view({'patch': 'patch'}), name='alterar_item_doacao')
]

busca_patterns = [
     path('busca/demandas', BuscaDemandasView.as_view({'get': 'list'}), name='buscas'),
     path('busca/ongs', BuscaOngsView.as_view({'get': 'list'}), name='buscas'),
]

teste_email = [
    path('email/', test_email),
]

urlpatterns = autenticacao_patterns + usuario_patterns + ong_patterns + demanda_patterns + doacao_patterns \
              + item_doacao + busca_patterns
urlpatterns +=teste_email
