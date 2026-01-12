print("Projeto de dados em construção")

from extract import extract_alunos
from transform import transform_alunos
from load import load_csv

def main():
    df = extract_alunos()
    df = transform_alunos(df)
    lista_validos= ['Aprovado', 'Reprovado']
    df_tratados = df[df['status_aprovação'].isin(lista_validos)]
    df_erros = df[~df['status_aprovação'].isin(lista_validos)]
    load_csv(df_tratados, 'alunos_tratados.csv')
    load_csv(df_erros, 'relatorio_erros.csv')

if __name__ == "__main__":
    main()