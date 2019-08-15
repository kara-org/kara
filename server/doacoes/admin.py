from django.contrib import admin
from .models import  *

@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    model = Status

@admin.register(Demanda)
class DemandaAdmin(admin.ModelAdmin):
    model = Demanda

@admin.register(Doacao)
class DoacaoAdmin(admin.ModelAdmin):
    model = Doacao

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    model = Categoria