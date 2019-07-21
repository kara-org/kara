from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.db.models import Q

from .models import *
from .serializers import *


class CategoriaView(viewsets.ViewSet):
    serializer_class = CategoriaSerializer

    def list(self, request):

        categoria= Categoria.objects.all()
        serializer = self.serializer_class(categoria, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(data= data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoriaDetailView(viewsets.ViewSet):

    serializer_class = CampanhaSerializer
    queryset = Categoria.objects.all()

    def get_object(self, id):
        try:
            return Categoria.objects.get(id = id, desabilitado=False)
        except Categoria.DoesNotExist:
            raise Http404

    def get(self, request, pk, formar=True):
        obj = self.get_object(pk)
        if obj: 
            serializer = self.serializer_class(obj)
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

    # def delete(self, request, pk, *args, **kwargs):
    #     obj = self.get_object(pk)
    #     request.data['desabilitado'] = True
    #     serializer = self.serializer_class(obj, data=request.data, partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CampanhaView(viewsets.ViewSet):
    serializer_class = CampanhaSerializer

    def list(self, request):

        campanha = Campanha.objects.all()
        serializer = self.serializer_class(campanha, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(data= data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CamapanhaDetailView(viewsets.ViewSet):

    serializer_class = CampanhaSerializer
    queryset = Campanha.objects.all()

    def get_object(self, id):
        try:
            return Campanha.objects.get(id = id, desabilitado=False)
        except Campanha.DoesNotExist:
            raise Http404

    def get(self, request, pk, formar=True):
        obj = self.get_object(pk)
        if obj: 
            serializer = self.serializer_class(obj)
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
        if obj:
            obj.delete()
            return Response(tatus=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    