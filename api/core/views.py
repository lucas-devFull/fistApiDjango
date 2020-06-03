from django.shortcuts import render
from rest_framework import viewsets
from .models import Cliente
from .models import Endereco
from .serializers import ClienteSerializer, EnderecoSerializer

class ClienteViewSet(viewsets.ModelViewSet):
        queryset =  Cliente.objects.filter()
        serializer_class = ClienteSerializer
