import requests
import sqlite3
from datetime import datetime
import pandas as pd
"""
Esse código é para adquirir a previsão do tempo da cidade do Rio de Janeiro, através da API meteo
O banco de dados utilizado será o mesmo (sqlite)
"""

# Coordenadas da cidade do Rio de Janeiro
latitude = -22.9068
longitude = -43.1729

# Link da API
url = (
    f"https://api.open-meteo.com/v1/forecast?"
    f"latitude={latitude}&longitude={longitude}&hourly=surface_pressure&timezone=auto"
    # Define a latitude,longitude e a previsão por hora. timezone=auto detecta automaticamente o fuso-horário
)

response = requests.get(url)  # Faz a requisição
data = response.json()

horas = data['hourly']['time']
pressao = data['hourly']['surface_pressure']
# Aqui, ocorre a extração da pressão por hora

# Criação do dataframe
df = pd.DataFrame({
    'momento': pd.to_datetime(horas),
    'valor': pressao
})

# Conexão com banco de dados (sqlite)
conn = sqlite3.connect("clima.db")
cursor = conn.cursor()

# Criação da tabela, caso ela não exista e inserção de dados na mesma
cursor.execute('''
    CREATE TABLE IF NOT EXISTS previsao_pressao_atm (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        momento TIMESTAMP,
        valor FLOAT
    )
''')

df.to_sql('previsao_pressao_atm', conn, if_exists='append', index=False)

conn.commit()
conn.close()

print("Dados de pressão atmosférica salvos com sucesso.")
