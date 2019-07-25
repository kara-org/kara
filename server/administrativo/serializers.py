import re

from rest_framework import serializers, status
from django.core.exceptions import ValidationError
from django.db import IntegrityError

from .models import Usuario

REGEX_PASSWORD = re.compile('^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[#$^+=!*()@%&]).{8,50}$')


class SolicitacaoRecuperarSenhaUsuarioSerializer(serializers.ModelSerializer):
    class UsuarioSerializer(serializers.ModelSerializer):

        email = serializers.EmailField(max_length=255)

        class Meta:
            model = Usuario
            fields = (
                'email', 'password'
            )


class UsuarioSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(max_length=128, write_only=True)

    class Meta:
        model = Usuario
        fields = (
                    'email', 'password', 'password2'
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
