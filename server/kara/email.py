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
                'introducao': "Introducao: lorem ipsum set dolor",
                'informacao': "Informacao: lorem ipsum",
            },
            'interesse-doacao':
                {
                'tipo_email': 'Interesse de doação',
                'introducao': "Estamos muito felizes por você ter demonstrado o interesse de realizar uma doação utilizando nosso portal.",
                'informacao': "Orientamos que para efetivar a doação você deve entrar em contato com a ong para combinar a melhor forma, local e horário para a entrega das doações."
                'rodape': "A kara Doações agradece a sua colaboração.",
            },
            'cancelamento-doacao-usuario':
                {
                'tipo_email': 'Cancelamento de doação',
                'introducao': "Introducao: lorem ipsum set dolor",
                'informacao': "Informacao: lorem ipsum",
            },
            'cancelamento-doacao-ong':
                {
                'tipo_email': 'Cancelamento de doação',
                'introducao': "Introducao: lorem ipsum set dolor",
                'informacao': "Informacao: lorem ipsum",
            }
        }
    
    def send_mail(self, destinatarios, username=None, tipo_email=None):
        
        context = self.mensagens[tipo_email]
        if username != None:
            context['usuario'] = str(username)

        assunto_email = '[Kara Doações] Notificação do Kara Doações.'
        # mail_payload = get_template('doacao.html').render(context)
        
        remetente = "no_replay@karadoacoes.com.br"
        # email_composicao = EmailMessage(assunto_email, mail_payload, remetente, ['mayara.machado@dcomp.ufs.br',])
        # email_composicao.content_subtype = 'html'
        # email_composicao.send()
        
        destinatarios_list = []
        if destinatarios:
            destinatarios_list.append(destinatarios)
        
        msg_html = loader.render_to_string(
            'doacao.html',
            context
        )
                
        send_mail(
            assunto_email,
            'Corpo da mensagem',
            remetente,
            destinatarios_list,
            html_message=msg_html,
        )

