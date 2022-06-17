import pandas as pd
import numpy as np
import os

tabela = pd.read_csv(f"/content/drive/MyDrive/teste_target/faturamento_estados.csv")

tabela['Faturamento'] = tabela['Faturamento'].apply(lambda x: float(x.replace(".", "").replace(",", ".")))
tabela['Percente'] = (tabela['Faturamento'] / tabela['Faturamento'].sum()) * 100

print(tabela)