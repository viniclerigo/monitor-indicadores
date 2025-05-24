import requests
import pandas as pd
import os

def run_selic_etl():
    url = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.4189/dados?formato=json"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    df = pd.DataFrame(data)
    df['data'] = pd.to_datetime(df['data'], dayfirst=True)
    df['valor'] = pd.to_numeric(df['valor'], errors='coerce')

    os.makedirs("data", exist_ok=True)
    df.to_json("data/selic_mensal.json", index=False)
    df.to_csv("data/selic_mensal.csv", index=False)
    print("✔️ ETL da Taxa Selic finalizada com sucesso!")
