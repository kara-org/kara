from django.contrib import admin
from .models import  *

# Register your models here.


@admin.register(Endereco)
class EnderecoAdmin(admin.ModelAdmin):
    model = Endereco
    
@admin.register(Telefone)
class TelefoneAdmin(admin.ModelAdmin):
    model = Telefone

@admin.register(Ong)
class OngAdmin(admin.ModelAdmin):
    model = Ong 
    
    
@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    model = Status 

@admin.register(Demanda)
class DemandaAdmin(admin.ModelAdmin):
    model = Demanda 

@admin.register(Doacao)
class DoacaoAdmin(admin.ModelAdmin):
    model = Doacao 

@admin.register(UsuarioPertenceOng)
class UsuarioPertenceOngAdmin(admin.ModelAdmin):
    model = UsuarioPertenceOng 

