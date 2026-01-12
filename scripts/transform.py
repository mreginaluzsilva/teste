import pandas as pd

def transform_alunos(df): 
    """
    Função que define a regra de aprovação dos alunos
    
    Regra de aprovação:
    - nota_simulado >= 7
    - frequencia >= 0.75
    """

    #validação
    colunas_obrigatorias = ["nota_simulado", "frequencia"]
    for coluna in colunas_obrigatorias:
        if coluna not in df.columns:
            raise ValueError(f"Coluna obrigatória ausente: {coluna}")
    
    #transformação
    df["status_aprovação"] = df.apply(
    lambda linha: 
        "Aprovado" 
        if linha["nota_simulado"] >= 7 and linha["frequencia"] >= 0.75
        else "Reprovado",
    axis=1
)
    return df