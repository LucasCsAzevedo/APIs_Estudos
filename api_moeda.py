import requests
import json
import matplotlib.pyplot as plt

# cotacoes = requests.get('https://economia.awesomeapi.com.br/json/all') # Para pegar todos os valores, atualizado a cada 30s
cotacoes = requests.get('https://economia.awesomeapi.com.br/json/daily/USD-BRL/30') # Pego a cotação do Dólar dos últimos 30 dias
cotacoes_dict = cotacoes.json()

# print(f'Dólar: {cotacoes_dict}')
# print(f'Euro: {cotacoes_dict['EUR']['bid']}')
# print(f'Bitcoin: {cotacoes_dict['BTC']['bid']}')

# for idx, item in enumerate(cotacoes_dict):
#     print(f"Valor do Dólar, dia {idx}: {item['bid']}")

# lista_cotacoes = [float(item['bid']) for item in cotacoes_dict]
# print(lista_cotacoes)

# Cotações de um período
cotacoes_btc = requests.get('https://economia.awesomeapi.com.br/json/daily/BTC-BRL/360?start_date=20200101&end_date=20201031')
cotacoes_btc_dict = cotacoes_btc.json()

# for item in cotacoes_btc_dict:
#     print(item['bid'])

lista_cotacoes_btc = [float(item['bid']) for item in cotacoes_btc_dict]
lista_cotacoes_btc.reverse()

plt.figure(figsize=(15, 5))
plt.plot(lista_cotacoes_btc)
plt.show()
