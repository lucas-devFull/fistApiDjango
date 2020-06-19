from .models import busca
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
import json
class BuscadorViewSet(ModelViewSet):

    def create(self, request, *args, **kwargs):
        dados = request.data
        if "search" in dados:
            web_scrap = busca(search=dados['search'])
            print(dados['search'])
            retorno = web_scrap.buscador(search=dados['search'])

            if retorno:
                return Response(data=retorno)

            else:
                return Response({'status':False, 'msg': 'não foi possivel efetuar a operacao'})
        else:
            return  Response({"status": False, "msg": "não encontrado o paramentro 'search'"})


