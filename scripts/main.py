print("Projeto de dados em construção")

from extract import extract_alunos
from transform import transform_alunos
from load import load_alunos

def main():
    df = extract_alunos()
    df = transform_alunos(df)
    load_alunos(df)

if __name__ == "__main__":
    main()