import json
import requests
from pprint import pprint

link_db = 'https://praticaapi-418af-default-rtdb.firebaseio.com/'

# Criar uma venda no meu DB (POST)
dados = {
    'cliente': 'Magda',
    'preco': '300',
    'valor': 'Mouse Gamer'
}
requisicao = requests.post(f'{link_db}/Vendas/.json', data=json.dumps(dados))


# Criar um novo produto (POST)
dados = {
    'nome': 'Headset',
    'preco': 280,
    'quantidade': 98
}
requisicao = requests.post(f'{link_db}/Produto/.json', data=json.dumps(dados))


# Editar um dados no meu banco (PATCH)
dados = {
    'cliente': 'Barbara'
}
requisicao = requests.patch(f'{link_db}/Vendas/-OTdLCSE5yDrF6VhxR8F/.json', data=json.dumps(dados))

# Pegar uma venda específica ou todas as vendas (GET)
requisicao = requests.get(f'{link_db}/Vendas/.json')
dic_requisicao = requisicao.json()

for id_venda in dic_requisicao:
    cliente = dic_requisicao[id_venda]['cliente']
    if cliente == 'Magda':
        print(id_venda, flush=True)
        id_dona_magda = id_venda

# Deletar a venda da dona magda (DELETE)
requisicao =  requests.delete(f'{link_db}/Vendas/{id_dona_magda}/.json')
pprint(requisicao)
pprint(requisicao.text)