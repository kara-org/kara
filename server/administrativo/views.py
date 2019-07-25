from rest_framework import viewsets, status
from rest_framework.response import Response
from django.db.models import Q

from .models import *
from .serializers import *

from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny


@permission_classes((AllowAny, ))
class UsuarioView(viewsets.ViewSet):
    serializer_class = UsuarioSerializer

    def list(self, request):

        usuarios = Usuario.objects.filter(ativo=True)
        for u in usuarios:
            u.enderecos = Endereco.objects.filter(usuario=u.pk, desabilitado = False)
            u.telefones = Telefone.objects.filter(usuario=u.pk, desabilitado = False)
        serializer = self.serializer_class(usuarios, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(data= data)
        if serializer.is_valid():
            sucesso = serializer.save()
            if sucesso:
                return Response(serializer.data , status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UsuarioDetailView(viewsets.ViewSet):

    serializer_class = UsuarioSerializer
    queryset = Usuario.objects.all()

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
    
@permission_classes((AllowAny, ))
class ONGView(viewsets.ViewSet):
    serializer_class = OngSerializer

    def list(self, request):

        ongs = Ong.objects.filter(ativo=True)
        serializer = self.serializer_class(ongs, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(data= data)
        if serializer.is_valid():
            sucesso = serializer.save()
            if sucesso:
                return Response(serializer.data , status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
