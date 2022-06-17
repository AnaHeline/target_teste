import pandas as pd
import numpy as np
import os
import json

tabela = pd.read_json("/content/drive/MyDrive/teste_target/dados.json")

menor_valor = tabela[['valor']].min()
print("O menor valor de faturamento ocorrido em um dia do mês é:", menor_valor)

maior_valor = tabela[['valor']].max()
print("O menor valor de faturamento ocorrido em um dia do mês é:", maior_valor)

media_faturamento = tabela[tabela['valor'] != 0].mean()
rowns = tabela[tabela['valor'] >= media_faturamento[1]]
qtde = len(rowns.index)
print("Número de dias no mês em que o valor de faturamento diário foi superior à média mensal", qtde)
