# %%
import json
import requests
from pprint import pprint

# %%
link = 'https://servicodados.ibge.gov.br/api/v3/agregados/8418/periodos/2019/variaveis/12749?localidades=N2[1]'
informacoes = requests.get(link)
dict_informacoes = informacoes.json()

# %%
item = dict_informacoes[0]['variavel']
valor = dict_informacoes[0]['resultados'][0]['series'][0]['serie']['2019']
print(f'{item}: {valor}')
