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

from drf_yasg.utils import swagger_auto_schema
from django.shortcuts import render

from kara.email import *

from django.shortcuts import render

from kara.padronizacao_responser import PadronizacaoResponse

@permission_classes((AllowAny, ))
class DemandaView(viewsets.ViewSet):
    serializer_class = DemandaSerializer
    serializer_retorno_class = DemandaSerializerRetorno
    serializer_class_alteracao = DemandaSerializerAlteracao
    serializer_class_cancelamento = DemandaSerializerCancelamento
    response = PadronizacaoResponse()


    def get_object(self, id):
        try:
            return Demanda.objects.get(id=id, ativo=True)
        except Demanda.DoesNotExist:
            return None

    @swagger_auto_schema(operation_id='Lista de demandas',
                         operation_description='Lista de demandas',
                         responses={200: DemandaSerializerRetorno(many=True)})
    def list(self, request, id_ong):
        demandas = Demanda.objects.filter(ong_id=id_ong)
        serializer = self.serializer_retorno_class(demandas, many=True)
        return self.response.responseFormatado(True, 200, data=serializer.data) 

    @swagger_auto_schema(operation_id='Criar demandas',
                         operation_description='Criar demandas',
                         responses={200: DemandaSerializerRetorno(),
                                    403: 'Categoria não encontrada.'})
    def create(self, request, id_ong, *args, **kwargs):
        ong = Ong.objects.get(pk=id_ong)
        if not obj:
            return self.response.responseFormatado(False, 404, mensagem="Demanda não encontrada.")
        data = request.data
        serializer = self.serializer_class(data=data, context={'ong': ong})
        if serializer.is_valid():
            try:
                obj = serializer.save()
                serializer = self.serializer_retorno_class(obj)
                return self.response.responseFormatado(True, 200, data=serializer.data) 
            except Exception as e:
                print(e)
                return self.response.responseFormatado(False, 403, mensagem='Categoria não encontrada.')

        return self.response.responseFormatado(False, 422, mensagem=serializer.errors)

    @swagger_auto_schema(operation_id='Atualizar de demandas',
                         operation_description='Atualizar demandas',
                         request_body=DemandaSerializerAlteracao,
                         responses={200: DemandaSerializerRetorno(),
                                    400: 'Erro de processamento.',
                                    403: '',
                                    404: 'Demanda não encontrada.'})
    def put(self, request, pk, *args, **kwargs):
        obj = self.get_object(pk)
        if not obj:
            return self.response.responseFormatado(False, 404, mensagem="Demanda não encontrada.")
        try:
            serializer = self.serializer_class_alteracao(obj, data=request.data)
            if serializer.is_valid():
                    obj = serializer.save()
                    retorno = self.serializer_retorno_class(obj)
                    return self.response.responseFormatado(True, 200, data=retorno.data) 
            return self.response.responseFormatado(False, 403, mensagem=serializer.errors)
        except Exception as e:
            print(e)
            return self.response.responseFormatado(False, 400, mensagem="Erro de processamento.")

    @swagger_auto_schema(operation_id='Atualizar de demandas',
                         operation_description='Atualizar demandas',
                         request_body=DemandaSerializerAlteracao,
                         responses={200: DemandaSerializerRetorno(),
                                    400: 'Erro de processamento.',
                                    403: '',
                                    404: 'Demanda não encontrada.'})
    def patch(self, request, pk, *args, **kwargs):
        obj = self.get_object(pk)
        if not obj:
            return self.response.responseFormatado(False, 404, mensagem="Demanda não encontrada.")
        serializer = self.serializer_class_alteracao(obj, data=request.data, partial=True)
        if serializer.is_valid():
            obj = serializer.save()
            retorno = self.serializer_retorno_class(obj)
            return self.response.responseFormatado(True, 200, data=retorno.data) 
        return self.response.responseFormatado(False, 403, mensagem=serializer.errors)

    @swagger_auto_schema(operation_id='Deletar de demandas',
                         operation_description='Deletar demandas',
                         request_body=DemandaSerializerCancelamento,
                         responses={200: DemandaSerializerRetorno(),
                                    400: 'Erro de processamento.',
                                    403: '',
                                    404: 'Demanda não encontrada.'})
    def delete(self, request, pk, *args, **kwargs):
        obj = self.get_object(pk)
        if not obj:
            return self.response.responseFormatado(False, 404, mensagem="Demanda não encontrada.")
        
        if not obj.ativo:
             return self.response.responseFormatado(False, 404, mensagem="Demanda já cancelada.")
        
        request.data['ativo'] = False
        serializer = self.serializer_class_cancelamento(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return self.response.responseFormatado(True, 200, data=serializer.data) 

        return self.response.responseFormatado(False, 403, mensagem=serializer.errors)

@permission_classes((AllowAny, ))
class DemandaListView(viewsets.ViewSet):
    serializer_class = DemandaSerializer
    serializer_retorno_class = DemandaSerializerRetorno
    response = PadronizacaoResponse()

    @swagger_auto_schema(operation_id= 'Listar demandas',
                         operation_description='Lista de demandas',
                         responses={200: DemandaSerializerRetorno(many=True)})
    def list(self, request):
        demandas = Demanda.objects.all()
        serializer = self.serializer_retorno_class(demandas, many=True)
        return self.response.responseFormatado(True, 200, data=serializer.data) 

class DoacaoView(viewsets.ViewSet):
    serializer_class = DoacaoSerializer
    serializer_retorno_class = DoacaoSerializerRetornoCadastro
    serializer_lista_class = DoacaoSerializerLista
    response = PadronizacaoResponse()

    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            doacao = serializer.save()
            if doacao:
                serializer = self.serializer_lista_class(doacao)
                try:
                    EnviarEmail().send_mail(request.user.email, request.user.nome_completo, 'Interesse de doação')
                except Exception as e:
                    print(e)
                return self.response.responseFormatado(True, 200, data=serializer.data) 
        return self.response.responseFormatado(False, 403, mensagem=serializer.errors)

    def list(self, request, id_ong):
        doacoes = Doacao.objects.filter(item_doacao__demanda__ong__id=id_ong).distinct()
        # for doacao in doacoes:
        #     itens_doacao = ItemDoacao.objects.filter(doacao=doacao)
        #     doacao.itens_doacao = itens_doacao
        serializer = self.serializer_lista_class(doacoes, many=True)
        return self.response.responseFormatado(True, 200, data=serializer.data) 

class DoacaoViewUser(viewsets.ViewSet):
    #serializer_class = DoacaoSerializer
    serializer_lista_class = DoacaoSerializerLista
    response = PadronizacaoResponse()

    def list(self, request, id_user):
        
        doacoes = Doacao.objects.filter(usuario__id=id_user)
        for doacao in doacoes:
            itens_doacao = ItemDoacao.objects.filter(doacao=doacao)
            doacao.itens_doacao = itens_doacao
        serializer = self.serializer_lista_class(doacoes, many=True)
                
        return self.response.responseFormatado(True, 200, data=serializer.data) 

    def post(self, request, pk, *args, **kwargs):
        resposta = DoacaoDo(request)
        retorno = resposta.confirmarDoacao(pk)
        response = PadronizacaoResponse()
        if isinstance(retorno, tuple):
            return self.response.responseFormatado(False,retorno[0], mensagem=retorno[1])
        
        return self.response.responseFormatado(True, 200, data=retorno)

    # region def patch(self, request, pk, *args, **kwargs):
    #     doacao = Doacao.objects.get(pk=pk)
    #     serializer = self.serializer_class(doacao, data=request.data, partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    # endregion    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        resposta = DoacaoDo(request)
        retorno = resposta.cancelarDoacao(pk)
        response = PadronizacaoResponse()
        if isinstance(retorno, tuple):
            return self.response.responseFormatado(False,retorno[0], mensagem=retorno[1])
        
        return self.response.responseFormatado(True,200, data=retorno)

@permission_classes((AllowAny, ))  
class BuscaDemandasView(viewsets.ViewSet):
    serializer_class = DemandaSerializerRetorno
    response = PadronizacaoResponse()


    def list(self, request):
        demanda = Demanda.objects.filter(Q(ativo=True))
        serializer = self.serializer_class(demanda, many=True)
        return self.response.responseFormatado(True, 200, data=serializer.data) 

class ItemDoacaoView(viewsets.ViewSet):
    serializer_class = ItemDoacaoConfirmacaoSerializer
    serializer_class_alteracao = ItemDoacaoAlteracaoSerializer
    response = PadronizacaoResponse()


    def post(self, request, pk, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            qtd = Decimal(request.data["quantidade_efetivada"]).quantize(Decimal('.01'), rounding=ROUND_DOWN)
            resposta = DoacaoDo(request)
            retorno = resposta.confirmarItemDoacao(pk, qtd)
            if isinstance(retorno, tuple):
                return self.response.responseFormatado(False,retorno[0], mensagem=retorno[1])
            return self.response.responseFormatado(True, 200, data=retorno) 
        return self.response.responseFormatado(False, 403, mensagem=serializer.errors)

    def delete(self, request, pk, *args, **kwargs):
        try:
            obj = ItemDoacao.objects.get(pk=pk)
            status_item = StatusItemDoacao.objects.get(pk=2)
            if obj.status.pk == 2 or obj.status.pk ==3:
                return self.response.responseFormatado(False, 403, mensagem="Item doação finalizada.")
            else:
                obj.status = status_item
                obj.save()
                return self.response.responseFormatado(False, 200, mensagem="Item deletado com sucesso.")
        except Exception as e:
            print(e)
            return self.response.responseFormatado(False, 404, mensagem="Item não encontrado.")

    def patch(self, request, pk, *args, **kwargs):
        obj = ItemDoacao.objects.get(pk=pk)
        serializer = self.serializer_class_alteracao(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return self.responseFormatado(True, 200, data=serializer.data) 
        return self.response.responseFormatado(False, 403, mensagem=serializer.errors)

def test_email(request):
    try:
        EnviarEmail().send_mail('mayara.machado@dcomp.ufs.br',request.user.nome_completo, 'recuperar-senha')
    except:
        pass
    return render(request, 'doacao.html')
