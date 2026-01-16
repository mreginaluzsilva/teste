import logging
from extract import extract_alunos
from transform import transform_alunos
from load import load_csv

logging.basicConfig(
    filename= 'pipeline.log', ##onde escrever
    level= logging.INFO, ##escrever só coisas importantes (INFO)
    format= '%(asctime)s - %(levelname)s - %(message)s', ##como escrever
    datefmt= '%Y-%m-%d %H:%M:%S', ##formato da data
    encoding= 'utf-8' ##permitir acentos
)

def main():
    logging.info("Iniciando o pipeline ETL de alunos...")

    try:
        df = extract_alunos()
        logging.info(f"Extração concluída. {len(df)} linhas lidas.") ##lenght

        df = transform_alunos(df)
        logging.info("Transformação concluída.")

        lista_validos= ['Aprovado', 'Reprovado']
        df_tratados = df[df['status_aprovação'].isin(lista_validos)]
        df_erros = df[~df['status_aprovação'].isin(lista_validos)]
        
        load_csv(df_tratados, 'alunos_tratados.csv')
        logging.info(f"Arquivo de tratados salvo: {len(df_tratados)} registros.")

        load_csv(df_erros, 'relatorio_erros.csv')
        logging.info(f"Relatório de erros salvo {len(df_erros)} registros.")

    except Exception as e:
        logging.error(f"Ocorreu um erro crítico no pipeline: {e}") ##se der qualquer erro, o log grava o erro antes de fechar
        raise ##levanta o erro para o terminal

    logging.info("Pipeline finalizado com sucesso.")

if __name__ == "__main__":
    main()