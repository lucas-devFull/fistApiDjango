from rest_framework import serializers
from .models import Cliente, Endereco, Telefone
class EnderecoSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Endereco
        fields = ['rua', 'cidade']

class TelefoneControlller(serializers.ModelSerializer):
    class Meta:
        model = Telefone
        fields = ['telefone']
class ClienteSerializer(serializers.ModelSerializer):
    endereco = EnderecoSerializer()
    numeroCelular = TelefoneControlller()
    class Meta:
        model = Cliente
        fields = ['id', 'nome','endereco','idade', 'numeroCelular']