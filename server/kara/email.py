from django.core.mail import send_mail
from django.conf import settings
from .models import *

# Renderização do email
from django.template.loader import get_template
from django.core.mail import EmailMessage


def send_mail(self):
        nome = self.cleaned_data['nome']
        nome_da_empresa = self.cleaned_data['nome_da_empresa']
        razao_social = self.cleaned_data['razao_social']
        nome_fantasia = self.cleaned_data['nome_fantasia']
        cnpj = self.cleaned_data['cnpj']
        telefone = self.cleaned_data['telefone']
        cep = self.cleaned_data['cep']
        bairro = self.cleaned_data['bairro']
        endereco = self.cleaned_data['endereco']
        numero = self.cleaned_data['numero']
        complemento = self.cleaned_data['complemento']

        context = {
            'nome': nome,
            'nome_da_empresa': nome_da_empresa,
            'razao_social': razao_social,
            'nome_fantasia': nome_fantasia,
            'cnpj': cnpj,
            'telefone': telefone,
            'cep': cep,
            'bairro': bairro,
            'endereco': endereco,
            'numero': numero,
            'complemento': complemento,
        }

        assunto_email = '[ASES - Site] Uma nova associação foi cadastrada a partir do site.'
        mail_payload = get_template('email_template.html').render(context)
        destinatarios = EmailDestinatario.objects.all()