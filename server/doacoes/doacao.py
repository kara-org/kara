from .models import *
from .serializers import *
from rest_framework.response import Response
from django.db.models import Q
from django.http import Http404, HttpResponse
from datetime import datetime

class DoacaoDo():
    
    def __init__(self, request):
        self.request = request
    
    def cancelarDoacao(self, pk):
        serializer_cancelamento_class = DoacaoCancelamentoSerializer
        
        doacao = Doacao.objects.get(pk=pk)
        
        itens_doacao = ItemDoacao.objects.filter(Q(doacao=pk), ~Q(status=2))
        if itens_doacao.exists():
            itens_doacao.update(status=2)
            
            retorno = {
                'usuario' : self.request.user,
                'doacao' : doacao,
                'data_cancelamento' : datetime.now().date()
            }
            serializer = serializer_cancelamento_class(retorno)
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response({'message':'403 - Essa doação já foi cancelada.'}, status=status.HTTP_403_FORBIDDEN)