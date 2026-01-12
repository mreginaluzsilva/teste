import csv
import random
from faker import Faker # Importando a nova biblioteca

# Configuração
NUM_ALUNOS = 1000
CAMINHO_ARQUIVO = 'data/raw/alunos.csv'

# Inicializa o gerador de dados em Português
fake = Faker('pt_BR')

def gerar_dados_fake():
    print(f"Gerando {NUM_ALUNOS} alunos com nomes reais...")
    
    with open(CAMINHO_ARQUIVO, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['id', 'nome', 'idade', 'nota_simulado', 'frequencia', 'turma'])
        
        for i in range(1, NUM_ALUNOS + 1):
            id_aluno = i
            
            # A MÁGICA ACONTECE AQUI: Gera um nome aleatório real
            nome = fake.name() 
            
            idade = random.randint(16, 20)
            nota = round(random.uniform(0, 10), 1)
            freq = round(random.uniform(0.5, 1.0), 2)
            turma = random.choice(['A', 'B', 'C'])

            # Caos (Mantivemos a mesma lógica de erros)
            chance_erro = random.random()
            if chance_erro < 0.02: nota = random.randint(11, 15)
            elif chance_erro < 0.04: freq = -0.5
            elif chance_erro < 0.06: idade = ''
            elif chance_erro < 0.08: nota = ''
            
            writer.writerow([id_aluno, nome, idade, nota, freq, turma])

    print(f"Sucesso! Arquivo gerado em: {CAMINHO_ARQUIVO}")

if __name__ == "__main__":
    gerar_dados_fake()