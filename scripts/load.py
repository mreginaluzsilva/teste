import pandas as pd
import sqlite3
import os

def load_csv(df, nome_arquivo):
    caminho_completo = f"data/processed/{nome_arquivo}"
    df.to_csv(caminho_completo, index=False)

def load_to_db(df, nome_tbela):
    """
    Salva o DataFrame em um banco de dados SQLite local.
    """

    os.makedirs("data/processed", exist_ok=True) ##cria a pasta data/processed se ela não existir

    caminho_banco = "data/processed/banco_alunos.db" ##onde ficará o arquivo do banco

    conn = sqlite3.connect(caminho_banco) ##abre conexão com o banco

    df.to_sql(nome_tbela, conn, if_exists='replace', index=False) ## salva DataFrame como tabela SQL/'replace' se a tabela existir, apaga e cria uma nova/index=False não salva o índice numérico do Pandas

    conn.close() ##fecha conexão para não travar o arquivo