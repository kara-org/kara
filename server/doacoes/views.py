from rest_framework import viewsets, status
from rest_framework.response import Response
from django.db.models import Q
from django.http import Http404, HttpResponse
from random import randint
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from django.core.mail import send_mail
from .models import *
from .serializers import *
from administrativo.models import Ong
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from .doacao import *

@permission_classes((AllowAny, ))
class DemandaView(viewsets.ViewSet):
    serializer_class = DemandaSerializer
    serializer_retorno_class = DemandaSerializerRetorno
    serializer_class_alteracao = DemandaSerializerAlteracao

    def get_object(self, id):
        try:
            return Demanda.objects.get(id=id, ativo=True)
        except Demanda.DoesNotExist:
            raise Http404

    def list(self, request, id_ong):
        print(id_ong)
        demandas = Demanda.objects.filter(ong_id=id_ong)
        serializer = self.serializer_retorno_class(demandas, many=True)
        return Response(serializer.data)

    def create(self, request, id_ong, *args, **kwargs):
        ong = Ong.objects.get(pk=id_ong)
        data = request.data
        serializer = self.serializer_class(data=data, context={'ong': ong})
        if serializer.is_valid():
            demanda = serializer.save()
            serializer = self.serializer_retorno_class(demanda)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, *args, **kwargs):
        obj = self.get_object(pk)
        serializer = self.serializer_class_alteracao(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, *args, **kwargs):
        obj = self.get_object(pk)
        serializer = self.serializer_class_alteracao(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):
        obj = self.get_object(pk)
        # if not obj.ativo:
        #     return Response("Demanda já cancelada", status=status.HTTP_400_BAD_REQUEST)
        request.data['ativo'] = False
        serializer = self.serializer_class_alteracao(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@permission_classes((AllowAny, ))
class DemandaListView(viewsets.ViewSet):
    serializer_class = DemandaSerializer
    serializer_retorno_class = DemandaSerializerRetorno

    def list(self, request):
        demandas = Demanda.objects.all()
        serializer = self.serializer_retorno_class(demandas, many=True)
        return Response(serializer.data)

class DoacaoView(viewsets.ViewSet):
    serializer_class = DoacaoSerializer
    serializer_retorno_class = DoacaoSerializerRetornoCadastro
    serializer_lista_class = DoacaoSerializerLista

    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            doacao = serializer.save()
            if doacao:
                serializer = self.serializer_retorno_class(doacao)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, id_ong):
        doacoes = Doacao.objects.filter(item_doacao__demanda__ong__id=id_ong).distinct()
        # for doacao in doacoes:
        #         #     itens_doacao = ItemDoacao.objects.filter(doacao=doacao)
        #         #     doacao.itens_doacao = itens_doacao
        serializer = self.serializer_lista_class(doacoes, many=True)
        return Response(serializer.data)

class DoacaoViewUser(viewsets.ViewSet):
    serializer_class = DoacaoSerializer
    serializer_lista_class = DoacaoSerializerLista
    serializer_confirmacao_class = DoacaoConfirmacaoSerializer

    def list(self, request, id_user):
        doacoes = Doacao.objects.filter(usuario__id=id_user)
        for doacao in doacoes:
            itens_doacao = ItemDoacao.objects.filter(doacao=doacao)
            doacao.itens_doacao = itens_doacao
        serializer = self.serializer_lista_class(doacoes, many=True)
        return Response(serializer.data)

    def post(self, request, pk, *args, **kwargs):
        doacao = Doacao.objects.get(pk=pk)
        serializer = self.serializer_confirmacao_class(data=request.data, context={'doacao': doacao})
        if serializer.is_valid():
            if serializer.save():
                serializer = self.serializer_lista_class(data=request.data)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def patch(self, request, pk, *args, **kwargs):
    #     doacao = Doacao.objects.get(pk=pk)
    #     serializer = self.serializer_class(doacao, data=request.data, partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        resposta = DoacaoDo(request)
        return resposta.cancelarDoacao(pk)

@permission_classes((AllowAny, ))  
class BuscaDemandasView(viewsets.ViewSet):
    serializer_class = DemandaSerializerRetorno

    def list(self, request):
        demanda = Demanda.objects.filter(Q(data_fim__gte = datetime.now().date()), Q(ativo=True))
        serializer = self.serializer_class(demanda, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
