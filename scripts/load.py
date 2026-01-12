import pandas as pd

def load_csv(df, nome_arquivo):
    caminho_completo = f"data/processed/{nome_arquivo}"
    df.to_csv(caminho_completo, index=False)