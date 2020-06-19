from rest_framework import serializers
from .models import Cliente, Endereco, Telefone, Teste, Usuario
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

class TesteSerializer(serializers.ModelSerializer):
    sla = Teste.teste
    class Meta:
        model = Teste

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['codigo','nome','email','senha','admin']