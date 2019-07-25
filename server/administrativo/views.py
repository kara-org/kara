from rest_framework import viewsets, status
from rest_framework.response import Response
from django.db.models import Q

from .models import Usuario
from .serializers import UsuarioSerializer
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from django.core.mail import send_mail

# Create your views here.
class UsuarioView(viewsets.ViewSet):
    serializer_class = UsuarioSerializer

    def retrive(self, request):
        usuario = Usuario.objects.get(pk=request.user.pk)
        serializer = self.serializer_class(usuario)
        return Response(serializer.data)

@permission_classes((AllowAny, ))
class UView(viewsets.ViewSet):
    serializer_class = UsuarioSerializer

    def create(self, request):
        email = request.data['email']
        usuario = Usuario.objects.filter(email=email)
        serializer = self.serializer_class(usuario)
        send_mail('Kara recuperação de senha', 'para recuperar sua senha utilize o link google.com', 'administrativo@kara.org.br' , [usuario.email], fail_silently=False)
        return Response(serializer.data)

    def list(self, request):
        usuario = Usuario.objects.all()
        serializer = self.serializer_class(usuario, many=True)
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