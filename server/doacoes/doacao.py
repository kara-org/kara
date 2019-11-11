from .models import *
from rest_framework import status
from .serializers import *
from rest_framework.response import Response
from django.db.models import Q
from django.http import Http404, HttpResponse
from datetime import datetime

from kara.email import EnviarEmail

class DoacaoDo():
    
    def __init__(self, request):
        self.request = request
    
    def cancelarDoacao(self, pk):
        serializer_cancelamento_class = DoacaoCancelamentoSerializer
        
        doacao = Doacao.objects.get(pk=pk)
        
        itens_doacao = ItemDoacao.objects.filter(doacao=pk, status__pk=1)
        if itens_doacao.exists():
            status_item = StatusItemDoacao.objects.get(pk=2)
            itens_doacao.update(status=status_item)
            
            retorno = {
                # 'usuario' : self.request.user,
                'doacao': doacao,
                'data_cancelamento': datetime.now().date()
            }
            serializer = serializer_cancelamento_class(retorno)
            try:
                EnviarEmail().send_mail(self.request.user.email,self.request.user.nome_completo, 'cancelamento-doacao-usuario')
            except Exception as e:
                print(e)
            
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response({'message': '403 - Essa doação já foi cancelada.'}, status=status.HTTP_403_FORBIDDEN)

    def confirmarDoacao(self, pk):
        doacao = Doacao.objects.get(pk=pk)
        itens_doacao = ItemDoacao.objects.filter(doacao=doacao)
        status_item = StatusItemDoacao.objects.get(pk=3)

        #verifica se todas as doacoes foram confirmadas
        if all((item.status.id == 3 or item.status.id == 2) for item in itens_doacao):
            return Response({'message': '403 - Essa doação está indisponível.'}, status=status.HTTP_403_FORBIDDEN)

        for item_doacao in itens_doacao:
            # Consulta os objetos
            demanda = Demanda.objects.get(pk=item_doacao.demanda.id)
            # Salva a quantidade do item doada e incrementa a quantidade alcançada da demanda
            item_doacao.quantidade_efetivada = item_doacao.quantidade_prometida

            if demanda.quantidade_alcancada:
                demanda.quantidade_alcancada += item_doacao.quantidade_prometida
            else:
                demanda.quantidade_alcancada = item_doacao.quantidade_prometida

            item_doacao.status = status_item
            item_doacao.save()
            doacao.data_confimacao = datetime.now()
            doacao.save()
            demanda.save()
            
        try:
            EnviarEmail().send_mail(self.request.user.email, self.request.user.nome_completo,  'confirmacao-doacao')
        except Exception as e:
            print(e)
            
        return Response({'message': 'Confirmada com sucesso'}, status=status.HTTP_202_ACCEPTED)

    def confirmarItemDoacao(self, pk, qtd):

        with transaction.atomic():
            try:
                item_doacao = ItemDoacao.objects.get(pk=pk)
                status_item = StatusItemDoacao.objects.get(pk=3)
                
                if item_doacao.status.pk == 3:
                    return Response({'message': '403 - Esse item doação já foi confirmado.'},
                                    status=status.HTTP_403_FORBIDDEN)
                elif item_doacao.status.pk == 2:
                    return Response({'message': '403 - Esse item doação foi cancelado.'},
                                    status=status.HTTP_403_FORBIDDEN)

                demanda = Demanda.objects.get(pk=item_doacao.demanda.id)

                #Salva a quantidade do item doada e incrementa a quantidade alcançada da demanda
                item_doacao.quantidade_efetivada = qtd
                if demanda.quantidade_alcancada:
                    demanda.quantidade_alcancada += qtd
                else:
                    demanda.quantidade_alcancada = qtd
                item_doacao.status = status_item
                item_doacao.save()
                demanda.save()
                return Response(status=status.HTTP_202_ACCEPTED)
            except:
                return Response({'message': "Doação não existe"}, status=status.HTTP_403_FORBIDDEN)
