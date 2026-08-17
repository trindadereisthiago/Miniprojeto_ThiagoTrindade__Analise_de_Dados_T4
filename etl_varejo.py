import pandas as pd
import csv
import re

path = ("Base Varejo.csv")

with open(path, mode="r", encoding="utf-8") as arquivo:
    leitor = csv.DictReader(arquivo, delimiter=";")
    dados = list(leitor)

df = pd.DataFrame(dados)

#verifica os tipos
print(df.dtypes)

def limpar_string(valor):
    valor = str(valor)
    valor = valor.strip()
    valor = re.sub(r"\s+", " ", valor)
    return valor

def converter_int(valor):
    return int(valor)

def converter_datetime(valor):
    return pd.to_datetime(valor, dayfirst=True)

colunas_string = ["CL_GENERO", "CL_SEG", "PR_CAT", "PR_NOME"]

for coluna in colunas_string:
    df[coluna] = df[coluna].apply(limpar_string)

colunas_int = ["CO_ID", "CL_ID", "CL_EC", "CL_FHL", "PR_ID"]

for coluna in colunas_int:
    df[coluna] = df[coluna].apply(converter_int)


colunas_datetime = ["DATA"]

for coluna in colunas_datetime:
    df[coluna] = df[coluna].apply(converter_datetime)


print(df.head())

print(df.dtypes)