import re

from rest_framework import serializers, status
from django.core.exceptions import ValidationError
from django.db import IntegrityError

from django.db import transaction

from .models import *

from kara.email import EnviarEmail

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
    endereco = EnderecoSerializer(allow_null=True, required=False)
    telefone = TelefoneSerializer(many=True, allow_null=True, required=False)

    class Meta:
        model = Usuario
        fields = (
                    'id', 'email', 'password', 'nome_completo', 'ativo',
                    'ultimo_login', 'cpf', 'foto','vinculo_ong',
                    'endereco','telefone', 'vinculo_ong',
                )
        
    def create(self, validated_data):
        print(validated_data)
        temEndereco = False
        if 'endereco' in validated_data:
            temEndereco, endereco = True, validated_data.pop("endereco")
        
        temTelefone = False
        if 'telefone' in validated_data:
            temTelefone, telefone = True, validated_data.pop("telefone")
        
        try:
            if temEndereco:
                end = Endereco(**endereco)
                end.save()
                user = Usuario.objects.create_user(endereco= end,  **validated_data)
            else:
                user = Usuario.objects.create_user( **validated_data)

            for t in telefone:
                fone = Telefone(**t)
                fone.save()
                user.telefone.add(fone)
            user.save()

            try:
                EnviarEmail().send_mail(user.email, user.nome_completo,'boas-vindas')
            except Exception as e:
                print(e)
            return user
        except Exception as e:
            print(e)
            return False
            # raise IntegrityError('Usuário já existe.')

class OngSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer(write_only=True, required=False)
    endereco = EnderecoSerializer(allow_null=True, required=False)
    telefone = TelefoneSerializer(many=True, allow_null=True, required=False)

    class Meta:
        model = Ong
        fields = ['id', 'nome', 'cnpj', 'historia', 'telefone', 'ativo' , 'usuario', 'endereco']

    def create(self, validated_data):
        usuario_data = validated_data.pop('usuario')
        
        endereco = validated_data.pop("endereco")
        telefone = validated_data.pop("telefone")
        
        ong, created = Ong.objects.get_or_create(cnpj = validated_data['cnpj'], defaults= validated_data)
        
        end, created = Endereco.objects.get_or_create(**endereco)
        if created:
            ong.endereco = end
            
        for t in telefone:
            fone = Telefone(**t)
            fone.save()
            ong.telefone.add(fone)
        
        ong.save()
        

        if ong:
            with transaction.atomic():
                """ endereco = usuario_data.pop("endereco") """
                telefone = usuario_data.pop("telefone")
                
                end, created = Endereco.objects.get_or_create(**endereco)
                
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
    telefone = TelefoneSerializer(many=True, allow_null=True)

    class Meta:
        model = Ong
        fields = ['id', 'nome', 'cnpj', 'historia', 'telefone', 'ativo', 'endereco']

class UsuarioOngSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128, write_only=True)
    endereco = EnderecoSerializer(allow_null=True, required=False)
    telefone = TelefoneSerializer(many=True, allow_null=True, required=False)
    ong = OngSerializer()

    class Meta:
        model = Usuario
        fields = (
                    'id', 'email', 'password', 'nome_completo', 'ativo',
                    'ultimo_login', 'cpf', 'foto','vinculo_ong',
                    'endereco','telefone', 'vinculo_ong', 'ong',
                )