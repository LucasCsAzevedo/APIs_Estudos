# API com paginação, vou trabalhar com uma do Banco Central
# Nessa aula, o professor explicou sobre usar o offset (primeiro)
# %%
import json
import requests
import pandas as pd
from pprint import pprint

# %%
link = 'https://olinda.bcb.gov.br/olinda/servico/mecir_dinheiro_em_circulacao/versao/v1/odata/informacoes_diarias?$top=1000&$skip=10000&$orderby=Data%20desc&$format=json'
requisicao = requests.get(link)
informacoes = requisicao.json()

# pprint(informacoes)

# %%
tabela = pd.DataFrame(informacoes['value'])
tabela
