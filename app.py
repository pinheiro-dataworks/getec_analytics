import streamlit as st
import pandas as pd
# import plotly.express as px
# import plotly.graph_objects as go
try:
    import plotly.express as px
    import plotly.graph_objects as go
except ImportError:
    import subprocess
    import sys
    subprocess.check_call([sys.executable, "-m", "pip", "install", "plotly"])
    import plotly.express as px
    import plotly.graph_objects as go
from pathlib import Path
import sys

# Adicionar pasta utils ao path
sys.path.append(str(Path(__file__).parent / 'utils'))

# Importa as funções criadas nos outros códigos do projeto para carregar dados e fazer cálculos 
from utils.data_loader import load_data, get_available_years
from utils.calculations import calculate_metrics, calculate_class_distribution, calculate_top_suppliers, calculate_group_performance

# Configuração da página
st.set_page_config(
    page_title="GETEC ANALYTICS",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS customizado
st.markdown("""
<style>
    [data-testid="stSidebar"] {
        background-color: #2b2b2b;
    }
    
    /* Cor branca para labels do sidebar */
    [data-testid="stSidebar"] label {
        color: white !important;
    }
    
    [data-testid="stSidebar"] .stMarkdown {
        color: white !important;
    }
    
    [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3 {
        color: white !important;
    }
    
    /* Seta de ocultar sidebar em branco */
    [data-testid="stSidebar"] button[kind="header"] {
        color: white !important;
    }

    [data-testid="stSidebar"] button[kind="header"] svg {
        fill: white !important;
        stroke: white !important;
    }

    [data-testid="collapsedControl"] {
        color: white !important;
    }

    [data-testid="collapsedControl"] svg {
        fill: white !important;
        stroke: white !important;
    }

    /* Ícone do botão de colapsar */
    [data-testid="baseButton-header"] {
        color: white !important;
    }

    [data-testid="baseButton-header"] svg {
        fill: white !important;
    }
            
    /* Forçar todos os SVGs do sidebar a ficarem brancos */
    [data-testid="stSidebar"] svg {
        fill: white !important;
        stroke: white !important;
    }

    .metric-card {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        min-height: 180px;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }

    .metric-card.green {
        background-color: #d4edda;
    }

    .metric-card.red {
        background-color: #f8d7da;
    }

    .footer {
        text-align: center;
        margin-top: 50px;
        padding: 20px;
        color: #666;
    }

    .social-links {
        position: fixed;
        top: 70px;
        right: 20px;
        z-index: 999;
    }

    .social-links a {
        margin-left: 10px;
        font-size: 24px;
        color: #333;
        text-decoration: none;
    }

    .alert-message {
        font-style: italic;
        color: #666;
        margin-top: 10px;
    }
</style>
""", unsafe_allow_html=True)

# Links sociais
st.markdown("""
<div class="social-links">
    <a href="https://www.linkedin.com/in/pinheiro-dataworks/" target="_blank">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="#0077b5">
            <path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/>
        </svg>
    </a>
    <a href="https://github.com/pinheiro-dataworks" target="_blank">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="#333">
            <path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/>
        </svg>
    </a>
</div>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    logo_path = Path("assets/images/pdw_white.png")
    if logo_path.exists():
        st.image(str(logo_path), width=200)

    st.markdown("---")

    if st.button("🔄 Recarregar dados", use_container_width=True): # botão de limpar o cache e recarregar os dados
        st.cache_data.clear()
        st.rerun()

    # Filtro para selecionar obra e ano
    st.markdown("---")
    st.subheader("Filtros")

    obra = st.selectbox("Obra", options=["Sunset", "Pharos"], index=0)

    expense_df, budget_df = load_data(obra)
    available_years = get_available_years(expense_df)

    ano = st.selectbox("Ano", options=available_years, index=0)

    st.markdown("---")

    if st.button("📥 Exportar dados processados", use_container_width=True): # botão para exporta os dados tratados
        st.info("Funcionalidade de exportação em desenvolvimento")

# Título
st.markdown('<div style="font-size: 32px; font-weight: bold;">GETEC ANALYTICS | <span style="font-size: 24px; font-style: italic;">Planeje certo. Gaste inteligente.</span></div>', unsafe_allow_html=True)
st.markdown("---")

# Carregar dados
expense_df, budget_df = load_data(obra)
metrics = calculate_metrics(expense_df, budget_df, ano)

# 1. Visão Geral
st.markdown("### 1. Visão Geral")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"""
    <div class="metric-card">
        <h4 style="margin-bottom: 15px;">Orçado</h4>
        <h2 style="margin: 15px 0;">R$ {metrics['orcado_valor']:,.2f}</h2>
        <p style="color: blue; font-size: 18px; margin-top: 15px;">{metrics['orcado_incc']:,.2f} INCC</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="metric-card">
        <h4 style="margin-bottom: 15px;">Executado</h4>
        <h2 style="margin: 15px 0;">R$ {metrics['executado_valor']:,.2f}</h2>
        <p style="color: blue; font-size: 18px; margin-top: 15px;">{metrics['executado_incc']:,.2f} INCC</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="metric-card">
        <h4 style="margin-bottom: 15px;">Saldo</h4>
        <h2 style="margin: 15px 0;">R$ {metrics['saldo_valor']:,.2f}</h2>
        <p style="color: blue; font-size: 18px; margin-top: 15px;">{metrics['saldo_incc']:,.2f} INCC</p>
    </div>
    """, unsafe_allow_html=True)

with col4:
    status_class = "green" if metrics['saldo_incc'] >= 0 else "red"
    status_text = "UnderBudget" if metrics['saldo_incc'] >= 0 else "OverBudget"
    st.markdown(f"""
    <div class="metric-card {status_class}">
        <h4 style="margin-bottom: 15px;">⚠️ Status Obra</h4>
        <h2 style="margin: 15px 0;">{status_text}</h2>
        <p style="font-size: 18px; margin-top: 15px; opacity: 0;">&nbsp;</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# 2. Evolução Temporal
st.markdown("### 2. Evolução Temporal dos Custos")
expense_year = expense_df[expense_df['ano_id'] == ano].copy()
months = [f"{ano}-{str(m).zfill(2)}" for m in range(1, 13)] #Criando a lista de meses no formato "YYYY-MM"
monthly_costs = [expense_year[expense_year['ano_mes'] == month]['custo_mes'].sum() for month in months]

monthly_df = pd.DataFrame({'Mês': months, 'Custo': monthly_costs}) #cria um gráfico de barras com os custos mensais
fig_monthly = px.bar(monthly_df, x='Mês', y='Custo', title='Custo Mensal', color_discrete_sequence=['#5DADE2'])
fig_monthly.update_layout(showlegend=False, xaxis_title="", yaxis_title="", title_x=0.5)
st.plotly_chart(fig_monthly, use_container_width=True)

st.markdown("---")

# 3. Distribuição
st.markdown("### 3. Distribuição de Recursos e Progresso")
col1, col2 = st.columns(2)

# Cria o gráfico de barras para distribuição por classe
with col1:
    class_dist = calculate_class_distribution(expense_df)
    fig_class = px.bar(class_dist, y='classe', x='custo', orientation='h', title='Classe de Despesas', color_discrete_sequence=['#F39C12'])
    fig_class.update_layout(showlegend=False, xaxis_title="", yaxis_title="", title_x=0.5)
    st.plotly_chart(fig_class, use_container_width=True)

# Cria o gráfico de rosca para evolução da obra
with col2:
    percentual_executado = (metrics['executado_incc'] / metrics['orcado_incc']) * 100 if metrics['orcado_incc'] > 0 else 0
    percentual_saldo = 100 - percentual_executado

    fig_donut = go.Figure(data=[go.Pie(
        labels=['Executado', 'Saldo'],
        values=[percentual_executado, percentual_saldo],
        hole=.6,
        marker_colors=['#8E44AD', '#D5D8DC'],
        direction='clockwise',
        sort=False
    )])
    fig_donut.update_layout(title='Evolução de Obra', title_x=0.5, showlegend=True,
                           annotations=[dict(text=f'{percentual_executado:.0f}%', x=0.5, y=0.5, font_size=30, showarrow=False)])
    st.plotly_chart(fig_donut, use_container_width=True)

st.markdown("---")

# 4. Performance
st.markdown("### 4. Performance por Grupo Orçamentário")
group_performance = calculate_group_performance(expense_df, budget_df)

def format_status(row): # Adciona status com emojis
    if row['Saldo'] < 0:
        return "🔴 Off-Track"
    elif row['Saldo'] == 0:
        return "🟡 On-Track"
    else:
        return "🟢 On-Track"

group_performance['Status'] = group_performance.apply(format_status, axis=1)
st.dataframe(group_performance, use_container_width=True, height=400)

# Exibe tabela interativa
off_track_count = len(group_performance[group_performance['Saldo'] < 0])
st.markdown(f'<p class="alert-message">Obra possui {off_track_count} grupo(s) com estouro de orçamento</p>', unsafe_allow_html=True)

st.markdown("---")

# 5. Top 10 - Fornecedores & Grupos
st.markdown("### 5. Top 10 | Líderes do Desembolso")
col1, col2 = st.columns(2)

# Gráfico dos 10 grupos orçamentários que mais gastaram
with col1:
    top_groups = calculate_top_suppliers(expense_df, 'grupo', 10)
    fig_groups = px.bar(top_groups, y='categoria', x='custo', orientation='h', title='Grupos Orçamentários', color_discrete_sequence=['#27AE60'])
    fig_groups.update_layout(showlegend=False, xaxis_title="", yaxis_title="", title_x=0.5)
    st.plotly_chart(fig_groups, use_container_width=True)

# Gráficos dos 10 fornecedores que mais receberam pagamentos
with col2:
    top_suppliers = calculate_top_suppliers(expense_df, 'credor', 10)
    fig_suppliers = px.bar(top_suppliers, y='categoria', x='custo', orientation='h', title='Fornecedores', color_discrete_sequence=['#8E44AD'])
    fig_suppliers.update_layout(showlegend=False, xaxis_title="", yaxis_title="", title_x=0.5)
    st.plotly_chart(fig_suppliers, use_container_width=True)

# Rodapé
st.markdown("---")
st.markdown("""
<div class="footer">
    <p>Desenvolvido por Renan Pinheiro</p>
    <p>V2026.01.02</p>
</div>
""", unsafe_allow_html=True)
