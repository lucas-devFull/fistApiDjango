from .models import Teste, Usuario
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .serializers import TesteSerializer, UsuarioSerializer
import json
from django.http import JsonResponse

# class ClienteViewSet(ModelViewSet):
        # queryset =  Cliente.objects.filter()
        # serializer_class = ClienteSerializer
# 
        # def list(self, request, *args, **kwargs):
                # print(self)
                # print(request.data)
                # queryset = self.get_queryset()
                # serializer = ClienteSerializer(queryset, many=True)
                # return Response("serializer.data")
# 
class Testaparametro(ModelViewSet):
        # queryset =  ""
        # serializer_class = TesteSerializer()

        def create(self, request, *args, **kwargs):
                dados = request.data
                sla = Teste(nome=dados['oi'])
                nome = sla.teste()
                return JsonResponse({'dados':nome})
                # return Response({"manDeuCerto" :sla.teste})

class testePost(ModelViewSet):
        queryset = Usuario.objects.filter()
        serializer_class = UsuarioSerializer