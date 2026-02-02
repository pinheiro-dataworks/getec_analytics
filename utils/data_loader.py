import pandas as pd
from pathlib import Path

def load_data(obra):
    """
    Carrega os dados de orçamento e despesas da obra selecionada
    """
    obra_lower = obra.lower()
    
    # Caminhos dos arquivos
    expense_path = Path(f"data/processed/{obra_lower}_expense.csv")
    budget_path = Path(f"data/processed/{obra_lower}_budget.csv")
    
    # Carregar dados (colunas separadas por ponto e vírgula, núemros decimais com vírugula e milhares com ponto)
    expense_df = pd.read_csv(expense_path, sep=';', decimal=',', thousands='.')
    budget_df = pd.read_csv(budget_path, sep=';', decimal=',', thousands='.')
    
    # Limpar espaços em branco
    expense_df.columns = expense_df.columns.str.strip()
    budget_df.columns = budget_df.columns.str.strip()
    
    # Converter colunas numéricas
    numeric_cols_expense = ['valor_documento', 'custo_mes', 'ano_id', 'mês_id', 'indice', 'incc_mes']
    numeric_cols_budget = ['valor_plan', 'incc_id', 'incc_plan']
    
    for col in numeric_cols_expense:
        if col in expense_df.columns:
            expense_df[col] = pd.to_numeric(expense_df[col], errors='coerce')
    
    for col in numeric_cols_budget:
        if col in budget_df.columns:
            budget_df[col] = pd.to_numeric(budget_df[col], errors='coerce')
    
    return expense_df, budget_df # devolve as duas tabelas carregadas e tratadas

# Retorna lista de anos disponíveis (dropna remove valores vazios, unique pega apenas valores únicos e sorted ordena do menor para o maior)
def get_available_years(expense_df):
    """
    Retorna lista de anos disponíveis nos dados
    """
    years = sorted(expense_df['ano_id'].dropna().unique())
    return [int(year) for year in years] # converte cada ano para núemro inteiro e retorna a lista