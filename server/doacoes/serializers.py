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
    quantidade_solicitada = serializers.DecimalField(max_digits=5, decimal_places=2, coerce_to_string=False)
    quantidade_alcancada = serializers.DecimalField(max_digits=5, decimal_places=2, coerce_to_string=False)
    
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
            
            print(validated_data)
        
            demanda = Demanda.objects.create(ong=ong_data, categoria=categoria, **validated_data)
            demanda.ong = ong_data
            return demanda
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
    quantidade_solicitada = serializers.DecimalField(max_digits=5, decimal_places=2, coerce_to_string=False)
    quantidade_alcancada = serializers.DecimalField(max_digits=5, decimal_places=2, coerce_to_string=False)

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
    ong = serializers.IntegerField()
    id_categoria = serializers.IntegerField()
    quantidade_solicitada = serializers.DecimalField(max_digits=5, decimal_places=2, coerce_to_string=False)
    quantidade_alcancada = serializers.DecimalField(max_digits=5, decimal_places=2, coerce_to_string=False)

    class Meta:
        model = Demanda
        fields = ['id',
                  'ong',
                  'id_categoria',
                  'quantidade_solicitada',
                  'quantidade_alcancada',
                  'descricao',
                  'ativo']
        
    def update(self, obj, validated_data):

        try:
            demanda = Demanda.objects.filter(pk=obj.pk)
            
            if 'ong' in validated_data:
                id_ong = validated_data.pop('ong')
                ong = Ong.objects.get(pk=id_ong)
                demanda[0].ong = ong
                
            if 'id_categoria' in validated_data:
                id_categoria = validated_data.pop('id_categoria')
                categoria = Categoria.objects.get(pk=id_categoria)
                demanda[0].categoria = categoria

            
            demanda[0].save()
            
            demanda.update( **validated_data)
                
            return demanda[0]
        except Exception as e:
            print(e)
            raise Exception

class DemandaSerializerCancelamento(serializers.ModelSerializer):
    ong = OngSerializer()
    quantidade_solicitada = serializers.DecimalField(max_digits=5, decimal_places=2, coerce_to_string=False)
    quantidade_alcancada = serializers.DecimalField(max_digits=5, decimal_places=2, coerce_to_string=False)

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
    quantidade_solicitada = serializers.DecimalField(max_digits=5, decimal_places=2, coerce_to_string=False)
    quantidade_alcancada = serializers.DecimalField(max_digits=5, decimal_places=2, coerce_to_string=False)
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
    quantidade_prometida = serializers.DecimalField(max_digits=5, decimal_places=2, coerce_to_string=False)

    class Meta:
        model = ItemDoacao
        fields = [
                    'quantidade_prometida',
                    'id_demanda'
                  ]

class ItemDoacaoListSerializer(serializers.ModelSerializer):
    demanda = DemandaSerializerRetorno()
    status = StatusItemDoacaoSerializer()
    quantidade_prometida = serializers.DecimalField(max_digits=5, decimal_places=2, coerce_to_string=False)
    quantidade_efetivada = serializers.DecimalField(max_digits=5, decimal_places=2, coerce_to_string=False)


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
    quantidade_efetivada = serializers.DecimalField(max_digits=5, decimal_places=2, coerce_to_string=False)


    class Meta:
        model = ItemDoacao
        fields = [
                    "quantidade_efetivada",
                  ]

class ItemDoacaoAlteracaoSerializer(serializers.ModelSerializer):
    quantidade_prometida = serializers.DecimalField(max_digits=5, decimal_places=2, coerce_to_string=False)

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
                    'item_doacao',
                  ]

    def create(self, validated_data):
        with transaction.atomic():
            try:
                itens_doacao = validated_data.pop("item_doacao")
                id_usuario = validated_data.pop("id_usuario")

                usuario = Usuario.objects.get(pk=id_usuario)
                status = StatusItemDoacao.objects.get(pk=1)
                doacao = Doacao.objects.create(usuario=usuario, **validated_data)
                items = []
                for item_doacao in itens_doacao:
                    id = int(item_doacao['id_demanda'])
                    quantidade = Decimal(item_doacao['quantidade_prometida']).quantize(Decimal('.01'),
                                                                                       rounding=ROUND_DOWN)
                    demanda = Demanda.objects.get(pk=id)
                    item = ItemDoacao(doacao=doacao, demanda=demanda, status=status, quantidade_prometida=quantidade)
                    item.save()
                    items.append(item)
                doacao.item_doacao.set(items)
                doacao.usuario = usuario
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