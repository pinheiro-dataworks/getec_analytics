# GETEC ANALYTICS | Planeje certo. Gaste inteligente.

## 📊 Visão Geral do Projeto

Dashboard interativo desenvolvido para análise e monitoramento dos custos de construção de dois empreendimentos residenciais em andamento. A solução oferece visibilidade completa sobre o desempenho financeiro das obras, permitindo tomadas de decisão estratégicas baseadas em dados consolidados e confiáveis.

## 🎯 Objetivo

O GETEC ANALYTIC foi desenvolvido para garantir a integridade da margem de lucro através do monitoramento contínuo do binômio **Prazo × Custo**.

Ao converter valores para o **INCC (Índice Nacional de Custo da Construção)**, o dashboard elimina distorções causadas pela inflação setorial, permitindo que gestores identifiquem se desvios orçamentários são resultado de falhas no planejamento interno ou de oscilações macroeconômicas externas.

A plataforma estabelece uma **"versão única da verdade"**, onde as áreas de engenharia e financeiro compartilham a mesma linguagem e base de dados, promovendo alinhamento estratégico e operacional.

## 💼 Benefícios para Incorporadora e Diretoria

A alta gestão obtém **previsibilidade** e **segurança** na tomada de decisões. Os principais benefícios incluem:

* **Mitigação Antecipada de Riscos**: Identificação precoce de desvios orçamentários em grupos específicos antes que comprometam o fluxo de caixa global

* **Transparência na Governança**: Sistema de indicadores visuais (verde/amarelo/vermelho) que permite gestão por exceção, focando a atenção da diretoria apenas nos pontos críticos

* **Poder de Negociação**: Visibilidade completa dos 10 maiores fornecedores, possibilitando negociações de volume e contratos globais mais vantajosos

* **Visibilidade do Saldo Remanescente**: Informação essencial para planejamento de novos lançamentos sem comprometer a liquidez operacional

## ⚙️ Melhoria dos Processos Internos

O dashboard atua como catalisador de eficiência operacional, transformando processos manuais em fluxos dinâmicos e automatizados:

* **Padronização da Informação**: Eliminação de planilhas paralelas através de uma base de dados única e atualizada

* **Agilidade no Ciclo de Feedback**: Gráficos de desembolso temporal permitem ajustes semanais no ritmo da obra ou aporte de recursos, substituindo análises mensais reativas

* **Accountability (Responsabilização)**: Classificação de custos por grupos orçamentários com rastreabilidade clara de performance por área e gestor, incentivando cultura de resultados

## 🚀 Funcionalidades

* **Visão Geral Executiva**: Cards com métricas principais (Orçado, Executado, Saldo e Status da Obra)

* **Evolução Temporal**: Gráfico de custos mensais com análise de tendências

* **Distribuição de Recursos**: Análise detalhada por classe de despesas e progresso físico da obra

* **Performance por Grupo**: Tabela detalhada com status de cada grupo orçamentário e indicadores de desvio

* **Top 10 Líderes**: Ranking de grupos orçamentários e fornecedores com maiores desembolsos acumulados

## 🛠️ Tecnologias Utilizadas

### Linguagens

* **Python** (versão 3.10+)

* **HTML/CSS** (estilização customizada no Streamlit)

### Bibliotecas

* **Streamlit** - Framework para criação de aplicações web interativas

* **Pandas** - Manipulação e análise de dados tabulares

* **Plotly** - Criação de gráficos interativos e visualizações dinâmicas

* **Pathlib** - Manipulação de caminhos de arquivos

* **sys** - Configuração de paths do Python

* **openpyxl** - Leitura e escrita de arquivos Excel (dependência do Pandas)

## 🔮 Roadmap: Evolução para Inteligência Preditiva (Machine Learning)

Com o dashboard estabelecido como base sólida de dados históricos, o próximo estágio evolutivo consiste em migrar de análises descritivas para **análises preditivas e prescritivas** utilizando Machine Learning.

### 1\. Análise de Viabilidade Preditiva

Utilização de dados históricos de obras anteriores para treinar modelos que estimem custos de novos empreendimentos com base em características básicas (localização, padrão construtivo, número de torres).

**Exemplo de output**: _"Dada a região X e o padrão Y, há 85% de probabilidade do custo de fundação exceder o orçamento em 12%."_

### 2\. Algoritmo de Tendência de Insumos

Integração com APIs de indicadores econômicos para previsão da curva do INCC e de insumos críticos (aço, concreto, cimento). Isso possibilitará **hedge de insumos** através de compras estratégicas antecipadas quando o modelo detectar tendências de alta iminente.

### 3\. Inteligência Geográfica e Regulatória (RegTech)

Cruzamento de dados de vendas (receita) com características técnicas e restrições legais regionais (zoneamento, taxa de ocupação, coeficiente de aproveitamento). O modelo identificará **"bolsões de oportunidade"** onde o custo de construção é menor e o VGV (Valor Geral de Vendas) é historicamente superior, otimizando a seleção de terrenos para novos empreendimentos.

### 4\. Score de Performance de Fornecedores

Desenvolvimento de modelo de classificação que considere não apenas faturamento, mas também:

* Histórico de atrasos de entrega

* Frequência de reajustes solicitados

* Qualidade da execução e conformidade técnica

O sistema sugerirá automaticamente o fornecedor mais adequado para cada tipo de serviço com base em score de eficiência histórica.
