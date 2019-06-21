from rest_framework import viewsets, status
from rest_framework.response import Response
from django.db.models import Q

from .models import Usuario
from .serializers import UsuarioSerializer


# Create your views here.
class UsuarioView(viewsets.ViewSet):
    serializer_class = UsuarioSerializer

    def list(self, request):

        usuarios = Usuario.objects.all()
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