# qual a forma de autenticação da API? 
# %%
import os
import requests
import pandas as pd
from io import StringIO

# %%
link = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey={os.getenv('chave_api')}&datatype=csv'

# %%
cotacoes = requests.get(link)

# %%
df = pd.read_csv(StringIO(cotacoes.text))
df.head(1)
