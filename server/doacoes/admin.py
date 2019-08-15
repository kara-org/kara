from django.contrib import admin
from .models import  *

@admin.register(StatusDoacao)
class StatusDoacaoAdmin(admin.ModelAdmin):
    model = StatusDoacao

@admin.register(StatusItemDoacao)
class StatusItemDoacaoAdmin(admin.ModelAdmin):
    model = StatusItemDoacao

@admin.register(Demanda)
class DemandaAdmin(admin.ModelAdmin):
    model = Demanda

@admin.register(Doacao)
class DoacaoAdmin(admin.ModelAdmin):
    model = Doacao

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    model = Categoria

@admin.register(ItemDoacao)
class ItemDoacaoAdmin(admin.ModelAdmin):
    model = ItemDoacao
