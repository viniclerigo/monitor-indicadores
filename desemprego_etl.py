import pandas as pd
import os
from request_helpers import fetch_data

def run_desemprego_etl():
    url = "https://servicodados.ibge.gov.br/api/v3/agregados/4099/periodos/all/variaveis/4099?localidades=N1[1]"
    json_data = fetch_data(url)

    resultados = json_data[0]['resultados'][0]['series'][0]['serie']
    df = pd.DataFrame(resultados.items(), columns=['periodo', 'taxa_desemprego'])

    # Ajuste dos dados
    df['periodo'] = pd.to_datetime(df['periodo'], format='%Y%m')
    df['taxa_desemprego'] = pd.to_numeric(df['taxa_desemprego'], errors='coerce')

    os.makedirs('data', exist_ok=True)
    df.to_json('data/desemprego_mensal.json', index=False)
    df.to_csv('data/desemprego_mensal.csv', index=False)
    print("✔️ ETL de desemprego finalizada com sucesso!")
