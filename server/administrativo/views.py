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
        request.data['ativo'] = False
        serializer = self.serializer_class(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ONGListView(viewsets.ViewSet):
    serializer_class = OngSerializer

    def list(self, request):
        ongs = Ong.objects.filter(ativo=True)
        serializer = self.serializer_class(ongs, many=True)
        return Response(serializer.data)

@permission_classes((AllowAny, ))
class OngCreateView(viewsets.ViewSet):
    serializer_class = OngSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(data= data)
        if serializer.is_valid():
            sucesso = serializer.save()
            if sucesso:
                return Response(serializer.data , status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@permission_classes((AllowAny, ))
class OngDetailView(viewsets.ViewSet):

    serializer_class = OngListSerializer
    queryset = Ong.objects.all()
    
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
            serializer = self.serializer_class(ong)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except:
            return Response({"message":"Esta ong não existe."}, status=status.HTTP_404_NOT_FOUND)
            

    def put(self, request, pk, *args, **kwargs):
        sucesso, _ =  self.valida_acesso( pk)        
        
        if sucesso: 
            obj = self.get_object(pk)
            serializer = self.serializer_class(obj, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"message":"Este usuário não tem acesso a esta ong."}, status=status.HTTP_403_FORBIDDEN)


    def patch(self, request, pk, *args, **kwargs):
        sucesso, _ =  self.valida_acesso( pk)        
        
        if sucesso: 
            obj = self.get_object(pk)
            serializer = self.serializer_class(obj, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"message":"Este usuário não tem acesso a esta ong."}, status=status.HTTP_403_FORBIDDEN)

    def delete(self, request, pk, *args, **kwargs):
        sucesso, _ =  self.valida_acesso(pk)        

        if sucesso: 
            obj = self.get_object(pk)
            request.data['ativo'] = False
            serializer = self.serializer_class(obj, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"message":"Este usuário não tem acesso a esta ong."}, status=status.HTTP_403_FORBIDDEN)
      