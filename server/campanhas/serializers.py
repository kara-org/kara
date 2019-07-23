from rest_framework import serializers, status
from .models import *

class CategoriaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Categoria
        # field = ['id', 'categoria']
        

class CampanhaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Campanha
        field = [
                'id'
                'titulo_campanha',
                'descricao',
                'produto',
                'quantidade',
                'unidade',
                'frequencia',
                'inicio_campanha',
                'fim_camapanha',
                'campanha_ilimitada',
                'categoria',
                'imagem',
        ]
        
    def create(self, validated_data):
        try:
            categoria_id = validated_data.pop('categoria')
            categoria = Categoria.objects.get(pk=categoria_id)
            
            obj = Campanha.objects.create(categoria=categoria, **validated_data)
            return obj
        except Exception as e:
            print(e)
        
        