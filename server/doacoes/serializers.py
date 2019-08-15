from rest_framework import serializers, status
from .models import *
from administrativo.models import Ong
from django.core.exceptions import ValidationError
from django.db import IntegrityError

from django.db import transaction

from .models import *

class DemandaSerializer(serializers.ModelSerializer):
    #cnpj_ong = serializers.IntegerField()
    id_categoria = serializers.IntegerField()
    class Meta:
        model = Demanda
        fields = ['id',
                  #'cnpj_ong',
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
                  'descricao']

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
                  'descricao']