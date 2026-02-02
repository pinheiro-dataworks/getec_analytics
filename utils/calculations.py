import pandas as pd

def calculate_metrics(expense_df, budget_df, ano=None):
    """
    Calcula as métricas principais do dashboard
    """
    # Orçado
    orcado_valor = budget_df['valor_plan'].sum() #valor em reais
    orcado_incc = budget_df['incc_plan'].sum()  #valor em INCC
    
    # Executado (filtrar por ano)
    if ano:
        expense_filtered = expense_df[expense_df['ano_id'] == ano]
    else:
        expense_filtered = expense_df
    
    executado_valor = expense_df['custo_mes'].sum()  # Total gasto acumulado em reais
    executado_incc = expense_df['incc_mes'].sum() # Total gasto acumulado em INCC
    
    # Saldo orçamentário
    saldo_valor = orcado_valor - executado_valor #em reais
    saldo_incc = orcado_incc - executado_incc #em INCC
    
    return {
        'orcado_valor': orcado_valor,
        'orcado_incc': orcado_incc,
        'executado_valor': executado_valor,
        'executado_incc': executado_incc,
        'saldo_valor': saldo_valor,
        'saldo_incc': saldo_incc
    }

# Gasto de cada categoria/classe
def calculate_class_distribution(expense_df):
    """
    Calcula a distribuição de custos por classe
    """
    class_dist = expense_df.groupby('classe')['custo_mes'].sum().reset_index() # agrupa os gastos por classe e soma os valores de cada
    class_dist.columns = ['classe', 'custo'] 
    class_dist = class_dist.sort_values('custo', ascending=True) # ordena do menor para o maior gasto
    
    return class_dist

# Identifica os maiores fornecedores ou grupos que mais gastaram
def calculate_top_suppliers(expense_df, column, top_n=10):
    """
    Calcula os top N fornecedores ou grupos
    """
    top_data = expense_df.groupby(column)['custo_mes'].sum().reset_index() #agrupa por fornecedor e soma os gastos
    top_data.columns = ['categoria', 'custo']
    top_data = top_data.sort_values('custo', ascending=False).head(top_n) #ordena do maior para o menor e pega apenas os top 10
    top_data = top_data.sort_values('custo', ascending=True) # inverte a ordem para facilitar a visualização
    
    return top_data

# Compara o planejado com o orçado real por grupo
def calculate_group_performance(expense_df, budget_df):
    """
    Calcula a performance por grupo orçamentário
    """
    # Orçado por grupo
    budget_group = budget_df.groupby('grupo')['incc_plan'].sum().reset_index() # soma o orçado por grupo
    budget_group.columns = ['Grupo', 'Orçado (INCC)']
    
    # Gasto por grupo
    expense_group = expense_df.groupby('grupo')['incc_mes'].sum().reset_index() # soma o gasto por grupo
    expense_group.columns = ['Grupo', 'Gasto (INCC)']
    
    # Junta as duas tabelas e preenche com zero onde não houver gasto
    performance = budget_group.merge(expense_group, on='Grupo', how='left')
    performance['Gasto (INCC)'] = performance['Gasto (INCC)'].fillna(0)
    
    # Calcula saldo de cada grupo
    performance['Saldo'] = performance['Orçado (INCC)'] - performance['Gasto (INCC)']
    
    # Formatar valores
    performance['Orçado (INCC)'] = performance['Orçado (INCC)'].round(2) # arredonda para 2 casas decimais
    performance['Gasto (INCC)'] = performance['Gasto (INCC)'].round(2)
    performance['Saldo'] = performance['Saldo'].round(2)
    
    return performance