from rest_framework import serializers, status
from .models import *
from administrativo.models import Ong, Usuario
from django.core.exceptions import ValidationError
from django.db import IntegrityError

from django.db import transaction

from .models import *

class DemandaSerializer(serializers.ModelSerializer):
    id_categoria = serializers.IntegerField()
    class Meta:
        model = Demanda
        fields = ['id',
                  'id_categoria',
                  'quantidade_solicitada',
                  'quantidade_alcancada',
                  'data_inicio',
                  'data_fim',
                  'descricao']

    def create(self, validated_data):
        id_categoria = validated_data.pop("id_categoria")
        ong_data = self.context.get("ong")
        categoria = Categoria.objects.get(pk=id_categoria)
        demanda = Demanda.objects.create(ong=ong_data, categoria=categoria, **validated_data)
        if demanda:
            return demanda
        return Demanda.objects.none()

class DemandaSerializerRetorno(serializers.ModelSerializer):
    #cnpj_ong = serializers.IntegerField()
    #id_categoria = serializers.IntegerField()
    class Meta:
        model = Demanda
        fields = ['id',
                  'ong',
                  'categoria',
                  'quantidade_solicitada',
                  'quantidade_alcancada',
                  'data_inicio',
                  'data_fim',
                  'descricao',
                  'ativo']

class DemandaSerializerAlteracao(serializers.ModelSerializer):
    class Meta:
        model = Demanda
        fields = ['id',
                  'ong',
                  'categoria',
                  'quantidade_solicitada',
                  'quantidade_alcancada',
                  'data_inicio',
                  'data_fim',
                  'descricao',
                  'ativo']

class DemandaSerializerList(serializers.ModelSerializer):
    class Meta:
        model = Demanda
        fields = ['id',
                  'ong',
                  'categoria',
                  'quantidade_solicitada',
                  'quantidade_alcancada',
                  'data_inicio',
                  'data_fim',
                  'descricao',
                  'ativo']

class ItemDoacaoCadastroSerializer(serializers.ModelSerializer):
    id_demanda = serializers.IntegerField()

    class Meta:
        model = ItemDoacao
        fields = [
                    'quantidade_prometida',
                    'id_demanda'
                  ]

class DoacaoSerializer(serializers.ModelSerializer):
    item_doacao = ItemDoacaoCadastroSerializer(many=True)

    class Meta:
        model = Doacao
        fields = [
                    'id_usuario',
                    'quantidade_reservada',
                    'data_agendamento',
                    'item_doacao'
                  ]

    def create(self, validated_data):
        itens_doacao = validated_data.pop("item_doacao")
        id_usuario = validated_data.pop("id_usuario")

        usuario = Usuario.objects.get(pk=id_usuario)
        demanda = Demanda.objects.get(pk=itens_doacao[0].id_demanda)
        status = StatusItemDoacao.objects.get(pk=1)

        doacao = Doacao.objects.create(usuario=usuario, **validated_data)

        try:
            for item_doacao in itens_doacao:
                item = ItemDoacao(doacao=doacao, demanda=demanda, status=status, **item_doacao)
                item.save()
            return doacao
        except Exception as e:
            print(e)
            return False