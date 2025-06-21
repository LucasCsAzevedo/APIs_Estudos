# endpoint, link de uma api que consigo fazer requisições

import json
import requests


cep = '03372050'
link = f'https://viacep.com.br/ws/{cep}/json/'

consulta = requests.get(link)
# print(consulta.json()['ddd']) # Retorna um dicionário para nós!!!!!

dicionario_consulta = consulta.json()

for item in dicionario_consulta:
    print(f'{item}: {dicionario_consulta[item]}')