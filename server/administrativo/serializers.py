import re

from rest_framework import serializers, status
from django.core.exceptions import ValidationError
from django.db import IntegrityError

from django.db import transaction

from .models import *

REGEX_PASSWORD = re.compile('^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[#$^+=!*()@%&]).{8,50}$')

class EnderecoSerializer(serializers.ModelSerializer):
    desabilitado = serializers.BooleanField(write_only=True, required=False)

    class Meta:
        model = Endereco
        fields = ['id', 'logradouro', 'bairro',
                  'cidade', 'estado' , 'numero', 
                  'principal', 'desabilitado' ]

    def create(self, validated_data):
        usuario_id = validated_data.pop('usuario')
        usuario = Usuario.objects.get(id=usuario_id)

        novo_end = Endereco(usuario=usuario, **validated_data)
        novo_end.save()

        return novo_end
    
class TelefoneSerializer(serializers.ModelSerializer):
    desabilitado = serializers.BooleanField(write_only=True, required=False)

    class Meta:
        model = Telefone
        fields = ['id', 'numero', 'whatsapp', 'desabilitado' ]

    def create(self, validated_data):
        novo_telefone = Telefone( **validated_data)
        novo_telefone.save()

        return novo_telefone

class SolicitacaoRecuperarSenhaUsuarioSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)

    class Meta:
        model = Usuario
        fields = (
            'email', 'password'
        )

class UsuarioSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128, write_only=True)
    endereco = EnderecoSerializer(allow_null=True)
    telefone = TelefoneSerializer(many=True, allow_null=True)

    class Meta:
        model = Usuario
        fields = (
                    'id', 'email', 'password', 'nome_completo', 'ativo',
                    'ultimo_login', 'cpf', 'foto','vinculo_ong',
                    'endereco','telefone', 'vinculo_ong',
                )
        
    def create(self, validated_data):
        print(validated_data)
        endereco = validated_data.pop("endereco")
        telefone = validated_data.pop("telefone")
        
        try:
            end = Endereco(**endereco)
            end.save()
            
            user = Usuario.objects.create_user(endereco= end,  **validated_data)
            for t in telefone:
                fone = Telefone(**t)
                fone.save()
                user.telefone.add(fone)
            user.save()
        
            return user
        except Exception as e:
            print(e)
            return False
            # raise IntegrityError('Usuário já existe.')

class OngSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer(write_only=True)
    endereco = EnderecoSerializer(allow_null=True)

    class Meta:
        model = Ong
        fields = ['id', 'cnpj', 'historia', 'ativo' , 'usuario', 'endereco']

    def create(self, validated_data):
        usuario_data = validated_data.pop('usuario')
        
        ong, created = Ong.objects.get_or_create(**validated_data)

        if ong:
            with transaction.atomic():
                endereco = usuario_data.pop("endereco")
                telefone = usuario_data.pop("telefone")
                
                end = Endereco(**endereco)
                end.save()
                
                user = Usuario.objects.create_user(endereco= end,  **usuario_data)
                for t in telefone:
                    fone = Telefone(**t)
                    fone.save()
                    user.telefone.add(fone)
                user.save()
        
                upo = UsuarioPertenceOng(usuario=user, ong=ong)
                upo.save()
                print(upo)

        return ong

class OngListSerializer(serializers.ModelSerializer):
    endereco = EnderecoSerializer(allow_null=True)
    class Meta:
        model = Ong
        fields = ['id', 'cnpj', 'historia', 'ativo', 'endereco']