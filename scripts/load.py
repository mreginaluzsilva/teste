import pandas as pd
OUTPUT_PATH = "data/processed/alunos_tratados.csv"
def load_alunos(df):
    df.to_csv(OUTPUT_PATH, index=False)