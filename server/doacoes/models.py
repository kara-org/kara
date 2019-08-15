from django.db import models

class Status(models.Model):
    codigo_status = models.IntegerField("Código status")
    mensagem = models.CharField("Mensagem", max_length=255)

class Categoria(models.Model):
    descricao = models.CharField("Descrição", max_length=255)

class Demanda(models.Model):
    ong = models.ForeignKey("administrativo.Ong", on_delete=models.DO_NOTHING)
    categoria = models.ForeignKey("Categoria", on_delete=models.DO_NOTHING)
    #produto = models.CharField("Produto", max_length=255)
    quantidade_solicitada = models.IntegerField("Quantidade solicitada")
    quantidade_alcancada = models.IntegerField("Quantidade alcançada", blank=True, null=True)
    #unidade = models.CharField("Unidade", max_length=5)
    data_inicio = models.DateField("Data inicial")
    data_fim = models.DateField("Data fim")
    descricao = models.CharField("Descrição", max_length=255)
    #sem_limite = models.BooleanField(default=True)
    #status = models.ForeignKey("Status", on_delete=models.DO_NOTHING)

class Doacao(models.Model):
    usuario = models.OneToOneField("administrativo.Usuario", on_delete=models.DO_NOTHING)
    #ong = models.OneToOneField("Ong", on_delete=models.DO_NOTHING)
    quantidade_reservada = models.CharField("Quantidade reservada", max_length=20)
    data_agendamento = models.DateField("Data agendamento")
    status = models.ForeignKey("Status", on_delete=models.DO_NOTHING)

class ItemDoacao(models.Model):
    quantidade_prometida = models.IntegerField("Quantidade prometida")
    quantidade_efetivada = models.IntegerField("Quantidade efetivada")
    data_atualizacao = models.DateField("Data atualização")
    doacao = models.ForeignKey("Doacao", on_delete=models.DO_NOTHING)
    demanda = models.ForeignKey("Demanda", on_delete=models.DO_NOTHING)
