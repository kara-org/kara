from rest_framework import viewsets, status
from rest_framework.response import Response
from django.db.models import Q
from django.http import Http404, HttpResponse
import random
from random import randint
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from django.core.mail import send_mail
from .models import *
from .serializers import *
import string
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from doacoes.models import *
from doacoes.serializers import OngDemandas
from kara.email import EnviarEmail
from django.core.files.storage import FileSystemStorage
from kara.padronizacao_responser import *

def gerar_senha():
    senha_numerica = randint(1000, 9999)
    chars=(string.ascii_uppercase + string.ascii_lowercase)
    senha_letras = ''.join(random.choice(chars) for _ in range(4))
    senha = str(senha_numerica) + senha_letras
    senhalist = list(senha)
    random.shuffle(senhalist)
    return (''.join(senhalist))

@permission_classes((AllowAny, ))
class RecuperarSenhaUsuarioView(viewsets.ViewSet):
    serializer_class = UsuarioSerializer
    response = PadronizacaoResponse()

    def create(self, request):
        email = request.data['email']
        try:
            usuario = Usuario.objects.get(email=email)
        except:
            return Response({"mensagem": "404 - Usuário não encontrada."}, status=status.HTTP_404_NOT_FOUND)
        senha = gerar_senha()
        hashed_pwd = make_password(senha)
        #a = check_password(senha, hashed_pwd)
        usuario.password = hashed_pwd
        usuario.save()
        
        try:
            EnviarEmail().send_mail(usuario.email, None,  'recuperar-senha', senha)
        except Exception as e:
            print(e)
            
        
        # send_mail('Recuperação de senha portal Kara', 'Sua nova senha de acesso é: ' + senha, 'suporte@kara.org.br', [usuario.email], fail_silently=False)
        return Response()

@permission_classes((AllowAny, ))
class UsuarioView(viewsets.ViewSet):
    serializer_class = UsuarioSerializer
    serializer_class_usuario_ong = UsuarioOngSerializer
    response = PadronizacaoResponse()

    def retrive(self, request):
        try:
            usuario = Usuario.objects.get(pk=request.user.pk)
            if usuario.vinculo_ong:
                usuario.ong = UsuarioPertenceOng.objects.get(usuario=usuario).ong
                serializer = self.serializer_class_usuario_ong(usuario)
            else:
                serializer = self.serializer_class(usuario)
        except:
            return self.response.responseFormatado(False, 403, mensagem=serializer.errors)
        return self.response.responseFormatado(True, 200, data=serializer.data) 

    def list(self, request):
        print('ola')
        usuarios = Usuario.objects.filter(ativo=True)
        for u in usuarios:
            u.enderecos = Endereco.objects.filter(usuario=u.pk, desabilitado = False)
            u.telefones = Telefone.objects.filter(usuario=u.pk, desabilitado = False)
        serializer = self.serializer_class(usuarios, many=True)
        return self.response.responseFormatado(True, 200, data=serializer.data) 

    def create(self, request, *args, **kwargs):
        print(f"request: {request.data}")
        data = request.data
        serializer = self.serializer_class(data=data)
        if request.FILES:
            serializer.profile = request.FILES['profile']
            print(f"foto: {serializer.profile}")
        if serializer.is_valid():
            serializer = serializer.save()
            try:
                EnviarEmail().send_mail(request.data['email'], request.data['nome_completo'], 'boas-vindas')
            except Exception as e:
                print(e)
            return self.response.responseFormatado(True, 200, data=serializer.data) 
        return self.response.responseFormatado(False, 403, mensagem=serializer.errors)

class UsuarioDetailView(viewsets.ViewSet):

    serializer_class = UsuarioSerializer
    queryset = Usuario.objects.all()
    response = PadronizacaoResponse()

    def get_object(self, id):
        try:
            return Usuario.objects.get(id = id, ativo=True)
        except Usuario.DoesNotExist:
            raise Http404

    def get(self, request, pk, formar=True):
        obj = self.get_object(pk)
        if obj: 
            obj.enderecos = Endereco.objects.filter(usuario=pk,  desabilitado = False)
            obj.telefones = Telefone.objects.filter(usuario=pk,  desabilitado = False)
            serializer = self.serializer_class(obj)
            # disable = serializer.data.pop('desabilitado')
            # print(serializer.data)
            return self.response.responseFormatado(True, 200, data=serializer.data) 
        return self.response.responseFormatado(False, 403, mensagem=serializer.errors)

    def put(self, request, pk, *args, **kwargs):
        obj = self.get_object(pk)
        request.data['password'] = "a"
        print(request.data)
        serializer = self.serializer_class(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return self.response.responseFormatado(True, 200, data=serializer.data) 
        return self.response.responseFormatado(False, 403, mensagem=serializer.errors)

    def patch(self, request, pk, *args, **kwargs):
        obj = self.get_object(pk)
        serializer = self.serializer_class(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return self.response.responseFormatado(True, 200, data=serializer.data) 
        return self.response.responseFormatado(False, 403, mensagem=serializer.errors)

    def delete(self, request, pk, *args, **kwargs):
        obj = self.get_object(pk)
        request.data['ativo'] = False
        serializer = self.serializer_class(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return self.response.responseFormatado(True, 200, data=serializer.data) 
        return self.response.responseFormatado(False, 403, mensagem=serializer.errors)

@permission_classes((AllowAny, ))
class OngCreateListView(viewsets.ViewSet):
    serializer_class = OngSerializer
    response = PadronizacaoResponse()

    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(data= data)
        if serializer.is_valid():
            serializer.save()
            try:
                EnviarEmail().send_mail(request.data['usuario']['email'], request.data['usuario']['nome_completo'], 'boas-vindas')
            except Exception as e:
                print(e)
            return self.response.responseFormatado(True, 200, data=serializer.data) 
        return self.response.responseFormatado(False, 403, mensagem=serializer.errors)
    
    def list(self, request):
        ongs = Ong.objects.filter(ativo=True)
        serializer = self.serializer_class(ongs, many=True)
        return response.responseFormatado(True, 200, data=serializer.data) 

@permission_classes((AllowAny, ))
class OngDetailView(viewsets.ViewSet):

    serializer_class = OngListSerializer
    serializer_class_retorno = OngDemandas
    queryset = Ong.objects.all()
    response = PadronizacaoResponse()
   
    def valida_acesso(self, pk):
        pertence = UsuarioPertenceOng.objects.filter(usuario = self.request.user.pk, ong=pk)
        if pertence.exists():
            return True, pertence.first()
        else:
            return False, None 


    def get_object(self, id):
        try:
            return Ong.objects.get(id = id, ativo=True)
        except Ong.DoesNotExist:
            raise Http404

    def get(self, request, pk, formar=True):
        try:
            ong = self.get_object(pk)
            ong.demandas = Demanda.objects.filter(ong=pk)
            serializer = self.serializer_class_retorno(ong)
            return self.response.responseFormatado(True, 200, data=serializer.data) 
        except Exception as e:
            return self.response.responseFormatado(False, 404, mensagem= "Ong não encontrada.")        

    def put(self, request, pk, *args, **kwargs):
        sucesso, _ =  self.valida_acesso( pk)        
        
        if sucesso: 
            obj = self.get_object(pk)
            serializer = self.serializer_class(obj, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return self.response.responseFormatado(True, 200, data=serializer.data) 
            return self.response.responseFormatado(False, 403, mensagem=serializer.errors)
        return self.response.responseFormatado(False, 403, mensagem="Este usuário não tem acesso a esta ong.")

    def patch(self, request, pk, *args, **kwargs):
        sucesso, _ =  self.valida_acesso( pk)        
        
        if sucesso: 
            obj = self.get_object(pk)
            serializer = self.serializer_class(obj, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return self.response.responseFormatado(True, 200, data=serializer.data) 
            return self.response.responseFormatado(False, 403, mensagem=serializer.errors)
        return self.response.responseFormatado(False, 403, mensagem="Este usuário não tem acesso a esta ong.")

    def delete(self, request, pk, *args, **kwargs):
        sucesso, _ =  self.valida_acesso(pk)        

        if sucesso: 
            obj = self.get_object(pk)
            request.data['ativo'] = False
            serializer = self.serializer_class(obj, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return self.response.responseFormatado(True, 200, data=serializer.data) 
            return self.response.responseFormatado(False, 403, mensagem=serializer.errors)
        return self.response.responseFormatado(False, 403, mensagem="Este usuário não tem acesso a esta ong.")

class TelefoneView(viewsets.ViewSet):
    serializer_class = TelefoneSerializer
    response = PadronizacaoResponse()

    # def get_usuario(self, id):
    #     try:
    #         return Usuario.objects.get(id = id, ativo=True)
    #     except Usuario.DoesNotExist:
    #         raise Http404

    def list(self, request, pk_usr):
        usuario = self.get_usuario(pk_usr)
        if usuario:
            usuario_id = usuario.id 
        else:
            usuario_id = None

        telefones = Telefone.objects.filter(usuario=usuario_id, ativo=True)
        serializer = TelefoneSerializer(telefones, many=True)
      
        return self.response.responseFormatado(True, 200, data=serializer.data) 

    def create(self, request,pk_usr, *args, **kwargs):
        request.data['usuario'] = self.get_usuario(pk_usr).pk
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            # serializer.save()
            obj = TelefoneSerializer.create(self, request.data)
            serializer = TelefoneSerializer(obj)
            return self.response.responseFormatado(True, 200, data=serializer.data) 
        return self.response.responseFormatado(False, 403, mensagem=serializer.errors)

class TelefoneViewDetail(viewsets.ViewSet):
    serializers_class = TelefoneSerializer
    queryset = Telefone.objects.all()
    response = PadronizacaoResponse()

    def get_object(self, pk_usr, id):
        try:
            return Telefone.objects.get(id = id, usuario = pk_usr , ativo=True)
        except Usuario.DoesNotExist:
            raise Http404

    # def get(self, request,pk_usr, pk, formar=True):
    #     obj = self.get_object(pk_usr, pk)
    #     if obj:
    #         serializer = TelefoneSerializer(obj)
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk_usr, pk, *args, **kwargs):
        obj = self.get_object(pk_usr, pk)
        serializer = TelefoneSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return self.response.responseFormatado(True, 200, data=serializer.data) 
        return self.response.responseFormatado(False, 403, mensagem=serializer.errors)

    def patch(self, request,pk_usr, pk, *args, **kwargs):
        obj = self.get_object(pk_usr, pk)
        serializer = TelefoneSerializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return self.response.responseFormatado(True, 200, data=serializer.data) 
        return self.response.responseFormatado(False, 403, mensagem=serializer.errors)

    def delete(self, request,pk_usr, pk, *args, **kwargs):
        obj = self.get_object(pk_usr, pk)
        request.data['desabilitado'] = True
        serializer = TelefoneSerializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return self.response.responseFormatado(True, 200, data=serializer.data) 
        return self.response.responseFormatado(False, 403, mensagem=serializer.errors)

class BuscaOngsView(viewsets.ViewSet):
    serializer_class = OngSerializer
    response = PadronizacaoResponse()

    def list(self, request):

        ongs = Ong.objects.filter(ativo=True)
        serializer = self.serializer_class(ongs, many=True)
        return self.response.responseFormatado(True, 200, data=serializer.data) 
