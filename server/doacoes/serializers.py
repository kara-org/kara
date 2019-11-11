from rest_framework import serializers
from administrativo.models import Usuario, Ong
from django.db import transaction
from .models import *
import datetime
from decimal import *


from administrativo.serializers import UsuarioSerializer, OngSerializer, TelefoneSerializer, EnderecoSerializer


class CategoriaItemDoacaoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Categoria
        fields = [
                "id",
                "descricao"
            ]

#region Demanda
class DemandaSerializer(serializers.ModelSerializer):
    categoria = CategoriaItemDoacaoSerializer(required=False)
    id_categoria = serializers.IntegerField(required=False)
    
    class Meta:
        model = Demanda
        fields = ['id',
                  'categoria',
                  'id_categoria',
                  'quantidade_solicitada',
                  'quantidade_alcancada',
                  'descricao']

    def create(self, validated_data):
        id_categoria = validated_data.pop("id_categoria")
        ong_data = self.context.get("ong")
        try:
            categoria = Categoria.objects.get(pk=id_categoria)
        
            demanda = Demanda.objects.create(ong=ong_data, categoria=categoria, **validated_data)
            if demanda:
                return demanda
            return Demanda.objects.none()
        except Exception as e:
                print(e)
                return e

class OngDemandas(serializers.ModelSerializer):
    demandas = serializers.ListField(child=DemandaSerializer())
    telefone = TelefoneSerializer(many=True)
    endereco = EnderecoSerializer()

    class Meta:
        model = Ong
        fields = ['id', 'nome', 'cnpj', 'historia', 'telefone', 'ativo', 'endereco', 'demandas']

class DemandaSerializerRetorno(serializers.ModelSerializer):
    categoria = CategoriaItemDoacaoSerializer()

    ong = OngSerializer()

    class Meta:
        model = Demanda
        fields = ['id',
                  'ong',
                  'categoria',
                  'quantidade_solicitada',
                  'quantidade_alcancada',
                  'descricao',
                  'ativo']

class DemandaSerializerAlteracao(serializers.ModelSerializer):
    id_ong = serializers.IntegerField()
    id_categoria = serializers.IntegerField()

    class Meta:
        model = Demanda
        fields = ['id',
                  'id_ong',
                  'id_categoria',
                  'quantidade_solicitada',
                  'quantidade_alcancada',
                  'descricao',
                  'ativo']

class DemandaSerializerCancelamento(serializers.ModelSerializer):
    ong = OngSerializer()

    class Meta:
        model = Demanda
        fields = ['id',
                  'ong',
                  'categoria',
                  'quantidade_solicitada',
                  'quantidade_alcancada',
                  'descricao',
                  'ativo']

class DemandaSerializerList(serializers.ModelSerializer):
    categoria = CategoriaItemDoacaoSerializer()

    ong = OngSerializer()

    class Meta:
        model = Demanda
        fields = ['id',
                  'ong',
                  'categoria',
                  'quantidade_solicitada',
                  'quantidade_alcancada',
                  'descricao',
                  'ativo']
#endregion

#region Item Doação
class StatusItemDoacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusItemDoacao
        fields = [
            'codigo_status',
            'mensagem',
        ]

class ItemDoacaoCadastroSerializer(serializers.ModelSerializer):
    id_demanda = serializers.IntegerField()

    class Meta:
        model = ItemDoacao
        fields = [
                    'quantidade_prometida',
                    'id_demanda'
                  ]

class ItemDoacaoListSerializer(serializers.ModelSerializer):
    demanda = DemandaSerializerRetorno()
    status = StatusItemDoacaoSerializer()

    class Meta:
        model = ItemDoacao
        fields = [
            "id",
            "quantidade_prometida",
            "quantidade_efetivada",
            "data_atualizacao",
            "doacao",
            "demanda",
            "status"
        ]

class ItemDoacaoConfirmacaoSerializer(serializers.ModelSerializer):

    class Meta:
        model = ItemDoacao
        fields = [
                    "quantidade_efetivada",
                  ]

class ItemDoacaoAlteracaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemDoacao
        fields = [
                    'quantidade_prometida',
                  ]
#endregion

#region Doação
class DoacaoSerializer(serializers.ModelSerializer):
    item_doacao = ItemDoacaoCadastroSerializer(many=True)
    id_usuario = serializers.IntegerField()

    class Meta:
        model = Doacao
        fields = [
                    'id_usuario',
                    'item_doacao'
                  ]

    def create(self, validated_data):
        itens_doacao = validated_data.pop("item_doacao")
        id_usuario = validated_data.pop("id_usuario")

        usuario = Usuario.objects.get(pk=id_usuario)
        status = StatusItemDoacao.objects.get(pk=1)
        with transaction.atomic():
            doacao = Doacao.objects.create(usuario=usuario, **validated_data)

            try:
                for item_doacao in itens_doacao:
                    id = int(item_doacao['id_demanda'])
                    quantidade = Decimal(item_doacao['quantidade_prometida']).quantize(Decimal('.01'),
                                                                                       rounding=ROUND_DOWN)
                    demanda = Demanda.objects.get(pk=id)
                    item = ItemDoacao(doacao=doacao, demanda=demanda, status=status, quantidade_prometida=quantidade)
                    item.save()
                return doacao
            except Exception as e:
                print(e)
            return False

class DoacaoSerializerRetornoCadastro(serializers.ModelSerializer):
    # item_doacao = ItemDoacaoCadastroSerializer(many=True)

    class Meta:
        model = Doacao
        fields = [
                    "id"
                  ]

class DoacaoSerializerLista(serializers.ModelSerializer):
    item_doacao = ItemDoacaoListSerializer(many=True)
    usuario = UsuarioSerializer()
    class Meta:
        model = Doacao
        fields = [
                    "id",
                    "usuario",
                    "data_confimacao",
                    "item_doacao"
                  ]

class DoacaoCancelamentoSerializer(serializers.Serializer):
    doacao = DoacaoSerializerLista()
    data_cancelamento = serializers.DateField(initial=datetime.date.today)
    
#endregion