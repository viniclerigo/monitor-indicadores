import requests
import pandas as pd
import os
from datetime import datetime, timedelta

def run_cambio_dolar_etl():
    # Define intervalo de datas
    data_final = datetime.today()
    data_inicial = data_final - timedelta(days=3*365)
    data_inicial_str = data_inicial.strftime("%d/%m/%Y")
    data_final_str = data_final.strftime("%d/%m/%Y")

    # Monta a URL com intervalo
    url = (
        f"https://api.bcb.gov.br/dados/serie/bcdata.sgs.1/dados"
        f"?formato=json&dataInicial={data_inicial_str}&dataFinal={data_final_str}"
    )

    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    df = pd.DataFrame(data)
    df['data'] = pd.to_datetime(df['data'], dayfirst=True)
    df['valor'] = pd.to_numeric(df['valor'], errors='coerce')

    os.makedirs("data", exist_ok=True)
    df.to_json("data/cambio_dolar.json", index=False)
    df.to_csv("data/cambio_dolar.csv", index=False)
    print("✔️ ETL da cotação do dólar finalizada com sucesso!")

