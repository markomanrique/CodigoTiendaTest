from rest_framework import serializers
from tiandaAPI.models import Categoria

class CategoriaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Categoria


        fields = ["id","descripcion"] 
        