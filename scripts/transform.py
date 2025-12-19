import pandas as pd

def transform_alunos(df): #diferente do extract, essa função recebe dados, ela não lê arquivo nenhum
    df["status_aprovação"] = df["nota"].apply(
    lambda x: "Aprovado" if x >= 7 else "Reprovado"
)
    return df