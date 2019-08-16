from django.db import models


class StatusItemDoacao(models.Model):
    codigo_status = models.IntegerField("Código status")
    mensagem = models.CharField("Mensagem", max_length=255)

class Categoria(models.Model):
    descricao = models.CharField("Descrição", max_length=255)

class Demanda(models.Model):
    ong = models.ForeignKey("administrativo.Ong", related_name='demanda', on_delete=models.DO_NOTHING)
    categoria = models.ForeignKey("Categoria", related_name='demanda',on_delete=models.DO_NOTHING)
    quantidade_solicitada = models.IntegerField("Quantidade solicitada")
    quantidade_alcancada = models.IntegerField("Quantidade alcançada", blank=True, null=True)
    unidade = models.CharField("Unidade", max_length=5)
    data_inicio = models.DateField("Data inicial")
    data_fim = models.DateField("Data fim")
    descricao = models.CharField("Descrição", max_length=255)
    ativo = models.BooleanField("Ativo", default=True)

class Doacao(models.Model):
    usuario = models.ForeignKey("administrativo.Usuario", related_name='doacao', on_delete=models.DO_NOTHING)
    data_agendamento = models.DateField("Data agendamento")
    data_confimacao = models.DateField("Data agendamento", blank=True, null=True)

class ItemDoacao(models.Model):
    quantidade_prometida = models.IntegerField("Quantidade prometida")
    quantidade_efetivada = models.IntegerField("Quantidade efetivada", blank=True, null=True)
    data_atualizacao = models.DateTimeField("Data atualização", auto_now=True)
    doacao = models.ForeignKey("Doacao", related_name='item_doacao', on_delete=models.DO_NOTHING)
    demanda = models.ForeignKey("Demanda", related_name='item_doacao', on_delete=models.DO_NOTHING)
    status = models.ForeignKey("StatusItemDoacao", related_name='item_doacao', on_delete=models.DO_NOTHING)
