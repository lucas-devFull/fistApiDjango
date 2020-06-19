
import requests
import json
from bs4 import BeautifulSoup as bs


class busca():
    retorno = list()
    search = ""

    def __init__(self, search):
        self.retorno = list()
        self.search = search
        return None

    def buscador(self, search):

        if len(search) > 0:


            headers = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3163.100 Safari/537.36'
            }

            urls = [

                {
                    "url" : 'https://search3.pontofrio.com.br/busca?q=' + self.search,
                    "site" : 'pontofrio'
                },
                {
                    "url": 'https://buscas2.casasbahia.com.br/busca?q=' + self.search,
                    "site": 'casasbahia'
                },{
                    'url': 'https://www.submarino.com.br/busca/' + self.search,
                    'site': 'submarino'
                },
                {
                    "url": 'https://www.americanas.com.br/busca/' + self.search,
                    "site": 'americanas'
                },

            ]

            for url in urls:
                try:
                    r = requests.get(url['url'], headers=headers)
                except:
                    r = requests.get(url['url'], headers=headers)
                print(r.url)
                if url['site'] == 'submarino' or url['site'] == 'americanas':
                    self.metodoSoup(content=r.content, site=url['site'])
                else:
                    self.metodoQuebraSring(content=r.content, site=url['site'])

            return self.retorno

        else:
            return False


    def metodoSoup(self, content, site):
        try:
            html = bs(content, 'html.parser')
        except:
            html = bs(content, 'html.parser')


        lista_produtos = html.find(class_='product-grid')

        produtos = list()


        if lista_produtos:
            for item in lista_produtos:
                produtos.append(
                    {
                        'nome_produto': item.find('h2').text,
                        'preco': item.find(class_="PriceUI-bwhjk3-11").text,
                        'img': item.find('a')['href']
                    }
                )

        self.retorno.append(
            {
                'site': site,
                'produtos': produtos
            }
        )

    def metodoQuebraSring(self, content, site):
        stringpagina = content.decode("utf-8")
        jspagina = stringpagina.split("JSON.parse('")[1]
        dadosstring = jspagina.split(")")[0].replace("'", "")


        json_precos = json.loads(dadosstring);

        try:
            html = bs(content, 'html.parser')
        except:
            html = bs(content, 'html.parser')


        lista_produtos = html.find(class_="neemu-products-container").findAll(class_='nm-product-item')

        produtos = list()
        for item in lista_produtos:
            produtos.append(
                {
                   "nome_produto": item.find(class_="nm-product-name").find('a')['title'],
                    "img": item.find("img")['data-src'],
                    "id_produto": item['data-productid']
                }

            )

        for preco in json_precos['search']['items']:
            for produto in produtos:
                if preco['id'] == produto['id_produto']:
                    produto['preco'] = preco['price']
                    break


        self.retorno.append(
            {
                "site" : site,
                "produtos": produtos
            }
        )


