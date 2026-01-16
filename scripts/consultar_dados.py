import sqlite3
import pandas as pd

conn = sqlite3.connect("data/processed/banco_alunos.db") ##conecta com o banco sql

query = "SELECT * FROM alunos_tratados WHERE frequencia = 1.0" ##variável de acordo com o que quer consultar

df = pd.read_sql(query, conn) ##precisa de dois argumentos para rodar: query e a conxão

print("--- ALUNOS COM NOTA ACIMA DE 9 NO BANCO SQL ---")
print(df.head()) ##mostra os 5 primeiros
print(f"Total encontrado: {len(df)}")

conn.close() ##fechamento obrigatório para não travar o banco