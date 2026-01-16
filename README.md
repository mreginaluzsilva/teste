# 🎓 Pipeline ETL de Alunos

Projeto de Engenharia de Dados para processamento, validação e armazenamento de dados acadêmicos.

## 📋 Sobre o Projeto
Este projeto simula um pipeline **ETL (Extract, Transform, Load)** completo. O sistema processa dados brutos de alunos (gerados via script), aplica regras de negócio para validar consistência (notas, frequência, idade), separa registros inválidos para auditoria e armazena os dados confiáveis em um Banco de Dados SQL.

**Objetivo:** Demonstrar um fluxo profissional de tratamento de dados com rastreabilidade (Logs) e persistência em banco relacional.

## 🚀 Tecnologias Utilizadas
* **Python 3.12+**
* **Pandas:** Manipulação e transformação de dados.
* **SQLite:** Banco de dados relacional (Serverless).
* **Faker:** Geração de dados sintéticos realistas.
* **Logging:** Monitoramento e registro de execução.
* **Git/GitHub:** Versionamento de código.

## ⚙️ Arquitetura do Pipeline

1.  **Extract:** Leitura de arquivos CSV brutos (`data/raw`).
2.  **Transform:**
    * Limpeza de dados (tratamento de nulos).
    * Validação de Regras de Negócio (Nota entre 0-10, Frequência positiva).
    * Separação: Dados Válidos vs. Dados com Erro.
3.  **Load:**
    * ✅ **Dados Válidos:** Salvos na tabela `alunos_tartados` (SQLite).
    * ⚠️ **Dados Inválidos:** Salvos em `relatorio_erros.csv` para auditoria.

## 📂 Estrutura de Arquivos

projeto-etl/
│
├── data/
│   ├── raw/             # Onde fica o CSV bruto
│   └── processed/       # Onde o Banco de Dados e Relatórios são salvos
│
├── scripts/
│   ├── extract.py       # Módulo de leitura
│   ├── transform.py     # Lógica de validação e limpeza
│   ├── load.py          # Módulo de salvamento (CSV e SQL)
│   ├── main.py          # Orquestrador do pipeline (com Logs)
│   ├── gerar_fakes.py   # Gerador de massa de dados
│   └── consultar_dados.py # Script para testar o banco SQL
│
├── pipeline.log         # Diário de execução do sistema
├── requirements.txt     # Lista de dependências
└── README.md            # Documentação


## 🛠️ Como Executar

### 1. Preparar o ambiente
Certifique-se de ter o Python instalado. Recomenda-se usar um ambiente virtual:

```bash
# Windows
python -m venv .venv
.\.venv\Scripts\Activate

# Instalar dependências
pip install -r requirements.txt
```

### 2. Gerar dados de teste
Execute o script para criar 1.000 alunos com dados fictícios (nomes, notas e falhas propositais):
```bash
python scripts/gerar_fakes.py
```

### 3. Rodar o Pipeline ETL
Processe os dados. O terminal mostrará o progresso via Logs.
```bash
python scripts/main.py
```

### 4. Verificar os resultados
* Abra o arquivo `pipeline.log` para ver os detalhes da execução.
* Verifique a pasta `data/processed` para encontrar o `relatorio_erros.csv`.
* Para consultar o Banco de Dados, rode:
```bash
python scripts/consultar_dados.py
```

---
Desenvolvido para fins de estudo em Engenharia de Dados.