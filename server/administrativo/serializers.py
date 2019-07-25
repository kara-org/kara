import re

from rest_framework import serializers, status
from django.core.exceptions import ValidationError
from django.db import IntegrityError

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
    endereco = EnderecoSerializer()
    telefone = TelefoneSerializer(many=True)

    class Meta:
        model = Usuario
        fields = (
                    'id', 'email', 'password', 'nome_completo', 'ativo',
                    'ultimo_login', 'cpf', 'foto','vinculo_ong',
                    'endereco','telefone', 'vinculo_ong',
                )
        
    # def validate(self, data):
    #
    #     if data.get('password') and data.get('password2') and data.get('password') == data.get('password2'):
    #         if not re.match(REGEX_PASSWORD, data.get('password')):
    #             raise ValidationError('Senhas invalidas')
    #     else:
    #         raise ValidationError('Senhas invalidas')
    #
    #     return data
    #
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
    #
    # def update(self, instance, validated_data):
    #     instance.email = validated_data.get('email', instance.email)
    #     instance.password = validated_data.get('password', instance.password)
    #     instance.save()
    #
    #     return instance
