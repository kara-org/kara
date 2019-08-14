from django.db import models
from administrativo.models import Usuario


class Categoria(models.Model):
    categoria = models.CharField(max_length=100)
    
class Campanha(models.Model):
    FREQUENCIA_CHOICES = (
                            ("CAMPANHA", "Duração da campanha"),
                            ("DIARIA", "Diária"),
                            ("SEMANAL", "Semanal"),
                            ("MENSAL", "Mensal"),
                            ("TRIMESTRAL", "Trimestral"),
                            ("SEMESTRAL", "Semestral"),
                            ("ANUAL", "Anual"),
                        )
    
    UNIDADES_CHOICES = (
                            ("UNIDADE", "Unidade"),
                            ("LITROS", "Litros"),
                            ("MILILITROS", "Mililitros"),
                            ("GRAMAS", "Gramas"),
                            ("MILIGRAMAS", "Miligramas"),
                            ("QUILOGRAMAS", "Quilogramas"),
                        )
    
    
    
    titulo_campanha = models.CharField(max_length=255)
    descricao = models.TextField(blank=True, null=True)
    produto = models.CharField(max_length=255)
    quantidade = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    unidade = models.CharField(max_length=9, choices=UNIDADES_CHOICES, default="UNIDADE")
    frequencia = models.CharField(max_length=9, choices=FREQUENCIA_CHOICES, default="CAMPANHA")
    inicio_campanha = models.DateField()
    fim_camapanha = models.DateField(blank=True, null=True)
    campanha_ilimitada = models.BooleanField(default=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    imagem = models.ImageField(upload_to='camapanhas/%Y/%m', null=True, blank=True, max_length=255)
    usuario  = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)
