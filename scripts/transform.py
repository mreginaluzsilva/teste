import pandas as pd

def calcular_status(linha):
    """
    Função auxiliar para aplicar as regras linha a linha.
    """ 
    nota = linha['nota_simulado']
    freq = linha['frequencia']

    if pd.isna(nota) or pd.isna(freq): #primeiro vê se tem dados
        return "Dados Insuficientes"
    
    if (nota < 0) or (nota > 10): #vê se o dado é válido
        return "Nota Inválida"
    
    if (freq < 0) or (freq > 1.0): #vê se o dado é válido
        return "Frequência Inválida"
    
    if nota >= 7 and freq >= 0.75: #regra de aprovação
        return "Aprovado"
    else:
        return "Reprovado"

def transform_alunos(df): 
    """
    Função que define a regra de aprovação dos alunos
    
    Regra de aprovação:
    - nota_simulado >= 7
    - frequencia >= 0.75
    """

    #validação
    colunas_obrigatorias = ["nota_simulado", "frequencia", 'idade']
    for col in colunas_obrigatorias:
        if col not in df.columns:
            raise ValueError(f"Coluna obrigatória ausente: {col}")

    #autofill   
    df["idade"] = df["idade"].fillna(-1)

    #transformação
    df["status_aprovação"] = df.apply(calcular_status, axis=1
)
    return df