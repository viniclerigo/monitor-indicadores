import pandas as pd
import matplotlib.pyplot as plt

# Carregar dados já salvos
df = pd.read_csv("data/ipca_mensal.csv")

# Garantir que a coluna de datas está no formato correto
df['periodo'] = pd.to_datetime(df['periodo'])

# Plotar gráfico
plt.figure(figsize=(12, 6))
plt.plot(df['periodo'], df['ipca_mensal'], marker='o', linestyle='-')
plt.title("IPCA Mensal no Brasil")
plt.xlabel("Período")
plt.ylabel("Variação mensal (%)")
plt.grid(True)
plt.tight_layout()

# Mostrar
plt.show()