import pandas as pd

DATA_PATH = "data/raw/alunos.csv"

def extract_alunos():
    df = pd.read_csv(DATA_PATH)
    return df