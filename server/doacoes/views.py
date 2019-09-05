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
from decimal import *


from django.shortcuts import render

from kara.email import *

from django.shortcuts import render

@permission_classes((AllowAny, ))
class DemandaView(viewsets.ViewSet):
    serializer_class = DemandaSerializer
    serializer_retorno_class = DemandaSerializerRetorno
    serializer_class_alteracao = DemandaSerializerAlteracao
    serializer_class_cancelamento = DemandaSerializerCancelamento

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
        serializer = self.serializer_class_cancelamento(obj, data=request.data, partial=True)
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
                try:
                    EnviarEmail().send_mail(request.user.email, request.user.nome_completo, 'Interesse de doação')
                except Exception as e:
                    print(e)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, id_ong):
        doacoes = Doacao.objects.filter(item_doacao__demanda__ong__id=id_ong).distinct()
        # for doacao in doacoes:
        #     itens_doacao = ItemDoacao.objects.filter(doacao=doacao)
        #     doacao.itens_doacao = itens_doacao
        serializer = self.serializer_lista_class(doacoes, many=True)
        return Response(serializer.data)

class DoacaoViewUser(viewsets.ViewSet):
    #serializer_class = DoacaoSerializer
    serializer_lista_class = DoacaoSerializerLista

    def list(self, request, id_user):
        doacoes = Doacao.objects.filter(usuario__id=id_user)
        for doacao in doacoes:
            itens_doacao = ItemDoacao.objects.filter(doacao=doacao)
            doacao.itens_doacao = itens_doacao
        serializer = self.serializer_lista_class(doacoes, many=True)
        return Response(serializer.data)

    def post(self, request, pk, *args, **kwargs):
        resposta = DoacaoDo(request)
        return resposta.confirmarDoacao(pk)

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
        demanda = Demanda.objects.filter(Q(ativo=True))
        serializer = self.serializer_class(demanda, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ItemDoacaoView(viewsets.ViewSet):
    serializer_class = ItemDoacaoConfirmacaoSerializer
    serializer_class_alteracao = ItemDoacaoAlteracaoSerializer

    def post(self, request, pk, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            qtd = Decimal(request.data["quantidade_efetivada"]).quantize(Decimal('.01'), rounding=ROUND_DOWN)
            resposta = DoacaoDo(request)
            return resposta.confirmarItemDoacao(pk, qtd)

    def delete(self, request, pk, *args, **kwargs):
        try:
            obj = ItemDoacao.objects.get(pk=pk)
            status_item = StatusItemDoacao.objects.get(pk=2)
            if obj.status == status_item:
                return Response("Item doação já cancelado", status=status.HTTP_400_BAD_REQUEST)
            else:
                obj.status = status_item
                obj.save()
                return Response("Ok", status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response("Objeto não encontrado", status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, *args, **kwargs):
        obj = ItemDoacao.objects.get(pk=pk)
        serializer = self.serializer_class_alteracao(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def test_email(request):
    context = {
        'tipo_email' : "confirmacao_doacao",
        'introducao' : "Introducao: lorem ipsum set dolor",
        'username' : "coentro",
        'informacao' : "Informacao: lorem ipsum"
    }
    try:
        EnviarEmail().send_mail('mayara.machado@dcomp.ufs.br',request.user.nome_completo, 'boas-vindas')
    except:
        pass
    return render(request, 'doacao.html', context)
