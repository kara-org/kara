from django.contrib import admin
from .models import  *

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    model = Usuario 

@admin.register(Endereco)
class EnderecoAdmin(admin.ModelAdmin):
    model = Endereco
    
@admin.register(Telefone)
class TelefoneAdmin(admin.ModelAdmin):
    model = Telefone

@admin.register(Ong)
class OngAdmin(admin.ModelAdmin):
    model = Ong 

@admin.register(UsuarioPertenceOng)
class UsuarioPertenceOngAdmin(admin.ModelAdmin):
    model = UsuarioPertenceOng 

