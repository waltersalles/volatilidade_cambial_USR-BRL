
# volatilidade_cambial_garch.py

import pandas as pd
import matplotlib.pyplot as plt
from arch import arch_model

# Dados simulados de variação mensal do dólar frente ao real em 2024 (%)
data = {
    "Data": pd.date_range(start="2024-01-01", periods=12, freq='M'),
    "USD/BRL": [0.8, -1.0, 0.5, -0.3, 0.2, -0.1, 0.4, 0.3, -0.6, 0.9, -0.4, 0.7]
}

# Criando DataFrame
df = pd.DataFrame(data).set_index("Data")

# Série de retornos (variações)
returns = df["USD/BRL"]

# Modelo GARCH(1,1)
model = arch_model(returns, vol="Garch", p=1, q=1)
results = model.fit(disp="off")

# Volatilidade condicional estimada
volatility = results.conditional_volatility

# Plotando a volatilidade ao longo do tempo
plt.figure(figsize=(10, 6))
plt.plot(volatility, label="Volatilidade Condicional (GARCH)", color="tomato", linewidth=2)
plt.title("Volatilidade Mensal Estimada - USD/BRL (GARCH)", fontsize=14)
plt.xlabel("Mês")
plt.ylabel("Volatilidade (%)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
