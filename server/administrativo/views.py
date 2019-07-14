from rest_framework import viewsets, status
from rest_framework.response import Response
from django.db.models import Q

from .models import Usuario
from .serializers import *


# Create your views here.
class UsuarioView(viewsets.ViewSet):
    serializer_class = UsuarioSerializer

    def list(self, request):

        usuarios = Usuario.objects.filter(desabilitado=False)
        serializer = self.serializer_class(usuarios, many=True)
        return Response(serializer.data)


    # def retrieve(self, request, pk=None):
    #     """
    #     Descrição do método de Dados da bandeira
    #     """
    #     try:
    #         bandeira = Bandeira.objects.get(pk=pk)
    #         serializer = self.serializer_class(bandeira)
    #         return Response(serializer.data)
    #     except:
    #         return Response({"mensagem": "404 - Bandeira não encontrada."}, status=status.HTTP_404_NOT_FOUND)
    
    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(data= data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class UsuarioDetailView(viewsets.ViewSet):

    serializer_class = UsuarioSerializer
    queryset = Usuario.objects.all()

    def get_object(self, id):
        try:
            return Usuario.objects.get(id = id, desabilitado=False)
        except Usuario.DoesNotExist:
            raise Http404

    def get(self, request, pk, formar=True):
        obj = self.get_object(pk)
        if obj: 
            serializer = self.serializer_class(obj)
            # disable = serializer.data.pop('desabilitado')
            # print(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, *args, **kwargs):
        obj = self.get_object(pk)
        serializer = self.serializer_class(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, *args, **kwargs):
        obj = self.get_object(pk)
        serializer = self.serializer_class(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):
        obj = self.get_object(pk)
        request.data['desabilitado'] = True
        serializer = self.serializer_class(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class EnderecoView(viewsets.ViewSet):
    serializer_class = EnderecoSerializer

    def get_usuario(self, id):
        try:
            return Usuario.objects.get(id = id, desabilitado=False)
        except Usuario.DoesNotExist:
            raise Http404

    def list(self, request, pk_usr):
        usuario = self.get_usuario(pk_usr)
        if usuario:
            usuario_id = usuario.id 
        else:
            usuario_id = None

        enderecos = Endereco.objects.filter(usuario = usuario_id, desabilitado=False)
        serializer = EnderecoSerializer(enderecos, many=True)
      
        return Response(serializer.data)

    
    def create(self, request,pk_usr, *args, **kwargs):
        request.data['usuario'] = self.get_usuario(pk_usr).pk
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            # serializer.save()
            obj = EnderecoSerializer.create(self, request.data)
            serializer = EnderecoSerializer(obj)
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EnderecoViewDetail(viewsets.ViewSet):
    serializers_class = EnderecoSerializer
    queryset = Endereco.objects.all()

    def get_object(self, pk_usr, id):
        try:
            return Endereco.objects.get(id = id, usuario = pk_usr , desabilitado=False)
        except Usuario.DoesNotExist:
            raise Http404

    def get(self, request,pk_usr, pk, formar=True):
        obj = self.get_object(pk_usr, pk)
        if obj: 
            serializer = EnderecoSerializer(obj)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk_usr, pk, *args, **kwargs):
        obj = self.get_object(pk_usr, pk)
        serializer = EnderecoSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request,pk_usr, pk, *args, **kwargs):
        obj = self.get_object(pk_usr, pk)
        serializer = EnderecoSerializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request,pk_usr, pk, *args, **kwargs):
        obj = self.get_object(pk_usr, pk)
        request.data['desabilitado'] = True
        serializer = EnderecoSerializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)