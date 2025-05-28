import requests
import pandas as pd
import os

def run_pib_etl():
    url = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.4380/dados?formato=json"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    df = pd.DataFrame(data)
    df['data'] = pd.to_datetime(df['data'], dayfirst=True)
    df['valor'] = pd.to_numeric(df['valor'], errors='coerce')

    os.makedirs("data", exist_ok=True)
    df.to_json("data/pib_trimestral.json", index=False)
    df.to_csv("data/pib_trimestral.csv", index=False)
    print("✔️ ETL PIB trimestral finalizada com sucesso!")
