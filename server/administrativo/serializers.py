import re

from rest_framework import serializers, status
from django.core.exceptions import ValidationError
from django.db import IntegrityError

from .models import *

REGEX_PASSWORD = re.compile('^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[#$^+=!*()@%&]).{8,50}$')


class UsuarioSerializer(serializers.ModelSerializer):
    # password2 = serializers.CharField(max_length=128, read_only=True)

    class Meta:
        model = Usuario
        fields = (
                    'id', 'email', 'password', 'nome_completo', 'ultimo_login', 'cpf_cnpj', 'foto'
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
    # def create(self, validated_data):
    #
    #     obj, created = Usuario.objects.create_user(
    #         email=validated_data['email'],
    #         password=validated_data['password'],
    #     )
    #
    #     if not created:
    #         raise IntegrityError('Usuário já existe.')
    #     else:
    #         return obj
    #
    # def update(self, instance, validated_data):
    #     instance.email = validated_data.get('email', instance.email)
    #     instance.password = validated_data.get('password', instance.password)
    #     instance.save()
    #
    #     return instance

class EnderecoSerializer(serializers.ModelSerializer):
    desabilitado = serializers.BooleanField(write_only=True)

    class Meta:
        model = Endereco
        fields = ['usuario','id', 'logradouro', 'bairro', 'cidade', 'estado' , 'numero', 'principal', 'desabilitado' ]

    def create(self, validated_data):
        usuario_id = validated_data.pop('usuario')
        usuario = Usuario.objects.get(id=usuario_id)

        novo_end = Endereco(usuario=usuario, **validated_data)
        novo_end.save()

        return novo_end

class TelefoneSerializer(serializers.ModelSerializer):
    desabilitado = serializers.BooleanField(write_only=True)

    class Meta:
        model = Telefone
        fields = ['usuario','id', 'numero', 'whatsapp', 'desabilitado' ]

    def create(self, validated_data):
        usuario_id = validated_data.pop('usuario')
        usuario = Usuario.objects.get(id=usuario_id)

        novo_telefone = Telefone(usuario=usuario, **validated_data)
        novo_telefone.save()

        return novo_telefone