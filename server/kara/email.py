from django.core.mail import send_mail
from django.conf import settings
from django.template import loader


# Renderização do email
from django.template.loader import get_template
from django.core.mail import EmailMessage

class EnviarEmail():
    
    def __init__(self):
        self.mensagens = {
            'boas-vindas':
                {
                'tipo_email': 'Boas vindas',
                'introducao': "Introducao: lorem ipsum set dolor",
                'informacao': "Informacao: lorem ipsum",
            },
            'confirmacao-doacao':
                {
                'tipo_email': 'Confirmação de doação',
                'introducao': "Informamos que a ong a qual você demonstrou interesse, confirmou o recebimento de sua doação.",
                'informacao': "Em caso de qualquer dúvida orientamentos que entre em contato com a ong.",
                'rodape': "A kara Doações agradece a sua colaboração.",

            },
            'interesse-doacao':
                {
                'tipo_email': 'Interesse de doação',
                'introducao': "Estamos muito felizes por você ter demonstrado o interesse de realizar uma doação utilizando nosso portal.",
                'informacao': "Orientamos que para efetivar a doação você deve entrar em contato com a ong para combinar a melhor forma, local e horário para a entrega das doações.",
                'rodape': "A kara Doações agradece a sua colaboração.",
            },
            'cancelamento-doacao-usuario':
                {
                'tipo_email': 'Cancelamento de doação',
                'introducao': "Infelizmente a ong cancelou sua doação, caso ainda haja interesse retorne ao site e realize uma nova doação para quem ainda está a espera de ajuda.",
                'informacao': "Caso tenha alguma dúvida sobre o cancelamento orientamos que entre em contato com a ong para mais informações sobre sua doação.",
                'rodape': "A kara Doações agradece a sua colaboração.",
            },
            'cancelamento-doacao-ong':
                {
                'tipo_email': 'Cancelamento de doação',
                'introducao': "Introducao: lorem ipsum set dolor",
                'informacao': "Informacao: lorem ipsum",
            },
            'recuperar-senha' : {
                'tipo_email': 'Recuperar senha',
                'introducao': 'Sua nova senha de acesso é: ',
            },
        }
    
    def send_mail(self, destinatarios, username=None, tipo_email=None, senha=None):
        
        context = self.mensagens[tipo_email]
        if username != None:
            context['usuario'] = str(username)
        
        if senha != None:
            context['introducao'] += str(senha)

        assunto_email = '[Kara Doações] Notificação do Kara Doações.'
        # mail_payload = get_template('doacao.html').render(context)
        
        remetente = "no_replay@karadoacoes.com.br"
        # email_composicao = EmailMessage(assunto_email, mail_payload, remetente, ['mayara.machado@dcomp.ufs.br',])
        # email_composicao.content_subtype = 'html'
        # email_composicao.send()
        
        destinatarios_list = []
        if destinatarios:
            destinatarios_list.append(destinatarios)
            
        template = 'doacao.html' 
        if tipo_email == 'recuperar-senha':
            template = 'recuperar_senha.html'
        
        msg_html = loader.render_to_string(
            template,
            context
        )
                
        send_mail(
            assunto_email,
            'Corpo da mensagem',
            remetente,
            destinatarios_list,
            html_message=msg_html,
        )

