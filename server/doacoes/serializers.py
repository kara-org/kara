from rest_framework import serializers
from administrativo.models import Usuario, Ong
from django.db import transaction
from .models import *
import datetime

from administrativo.serializers import UsuarioSerializer, OngSerializer, TelefoneSerializer

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
    categoria = CategoriaItemDoacaoSerializer()
    ong = OngSerializer()
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
    categoria = CategoriaItemDoacaoSerializer()
    ong = OngSerializer()
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
    demanda = DemandaSerializerRetorno()

    class Meta:
        model = ItemDoacao
        fields = [
                    'quantidade_prometida',
                    'demanda'
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
    id_item = serializers.IntegerField()
    item_doacao = StatusItemDoacaoSerializer(read_only=True)

    class Meta:
        model = ItemDoacao
        fields = [
                    'id_item',
                    'quantidade_efetivada',
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
                    'data_agendamento',
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
                    quantidade = int(item_doacao['quantidade_prometida'])
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
    # itens_doacao = serializers.ListField(child=ItemDoacaoListSerializer())
    class Meta:
        model = Doacao
        fields = [
                    "id",
                    "usuario",
                    "data_agendamento",
                    "data_confimacao",
                    "item_doacao"
                  ]

class DoacaoConfirmacaoSerializer(serializers.ModelSerializer):
    item_doacao = ItemDoacaoConfirmacaoSerializer(many=True)

    class Meta:
        model = Doacao
        fields = [
                    "id",
                    "data_confimacao",
                    "item_doacao"
                  ]

    def create(self, validated_data):
        itens_doacao = validated_data.pop("item_doacao")
        doacao = self.context.get("doacao")

        #usuario = Usuario.objects.get(pk=id_usuario)
        status = StatusItemDoacao.objects.get(pk=3)
        with transaction.atomic():
            try:
                for item_doacao in itens_doacao:
                    #Captura os identificadores
                    id_item = int(item_doacao['id_item'])
                    #Consulta os objetos
                    item = ItemDoacao.objects.get(pk=id_item)
                    demanda = Demanda.objects.get(pk=item.demanda.id)
                    #Salva a quantidade do item doada e incrementa a quantidade alcançada da demanda
                    item.quantidade_efetivada = int(item_doacao['quantidade_efetivada'])
                    if demanda.quantidade_alcancada:
                        demanda.quantidade_alcancada += int(item_doacao['quantidade_efetivada'])
                    else:
                        demanda.quantidade_alcancada = int(item_doacao['quantidade_efetivada'])
                    item.status = status
                    item.save()
                    demanda.save()
                return True
            except Exception as e:
                print(e)
            return False

class DoacaoCancelamentoSerializer(serializers.Serializer):
    doacao = DoacaoSerializerLista()
    data_cancelamento = serializers.DateField(initial=datetime.date.today)
    
#endregion

class OngDemandas(serializers.ModelSerializer):
    demandas = serializers.ListField(child=DemandaSerializer())
    telefone = TelefoneSerializer(many=True)

    class Meta:
        model = Ong
        fields = ['id', 'nome', 'cnpj', 'historia', 'telefone', 'ativo', 'endereco', 'demandas']