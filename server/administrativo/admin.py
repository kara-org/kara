from django.contrib import admin
from .models import  *

# Register your models here.


@admin.register(Endereco)
class EnderecoAdmin(admin.ModelAdmin):
    model = Endereco
    
@admin.register(Telefone)
class TelefoneAdmin(admin.ModelAdmin):
    model = Telefone

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    model = Usuario 
