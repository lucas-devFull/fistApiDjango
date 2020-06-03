from django.shortcuts import render
from rest_framework import viewsets
from .models import Cliente
from .models import Endereco
# from .serializers import EnderecoSerializer
from .serializers import ClienteSerializer


# class EnderecoViewSet(viewsets.ModelViewSet):
        # queryset = Endereco.objects.all()
        # serializer_class = EnderecoSerializer

class ClienteViewSet(viewsets.ModelViewSet):
        queryset = Cliente.objects.all()
        serializer_class = ClienteSerializer

# Create your views here.
