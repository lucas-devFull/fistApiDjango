from rest_framework import serializers
from .models import Cliente
from .models import Endereco
# 
class EnderecoSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Endereco
        fields = ['id', 'rua', 'cidade']
class ClienteSerializer(serializers.ModelSerializer):
    endereco = EnderecoSerializer(many=True, read_only=True)
    class Meta:
        model = Cliente
        fields = ['id', 'nome','endereco','idade']