from utils.request_helpers import fetch_data
import pandas as pd
import os

def run_ipca_etl():
    url = "https://servicodados.ibge.gov.br/api/v3/agregados/1737/periodos/all/variaveis/63?localidades=N1[1]"
    json_data = fetch_data(url)

    resultados = json_data[0]['resultados'][0]['series'][0]['serie']
    df = pd.DataFrame(resultados.items(), columns=['periodo', 'ipca_mensal'])

    df['periodo'] = pd.to_datetime(df['periodo'], format="%Y%m")
    df['ipca_mensal'] = df['ipca_mensal'].astype(float)

    os.makedirs("data", exist_ok=True)
    df.to_csv("data/ipca_mensal.csv", index=False)
    print("✔️ IPCA ETL finalizada com sucesso!")
