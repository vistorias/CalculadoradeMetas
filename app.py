import streamlit as st
import pandas as pd

def calcular_meta(valor_mensal, indicadores):
    total_trimestral = valor_mensal * 3  # Meta trimestral inicial
    
    pesos = {
        'Produção': 0.15,
        'Ticket Médio': 0.15,
        'Despesas': 0.15,
        'Satisfação Cliente': 0.275,
        'Pesquisa Clima': 0.0688,
        'Turnover': 0.0688,
        'ABS': 0.0688,
        'Treinamento': 0.0688
    }
    
    total_recebido = total_trimestral
    
    for mes in indicadores:
        for indicador, ativo in mes.items():
            if not ativo:
                total_recebido -= valor_mensal * pesos[indicador]
    
    return total_recebido

# Configuração da página
st.set_page_config(page_title="Calculadora de Metas Trimestrais", layout="wide")
st.markdown("<h1 style='text-align: center;'>📊 Calculadora de Metas Trimestrais</h1>", unsafe_allow_html=True)

valor_mensal = st.number_input("Digite o valor mensal da meta:", min_value=0.0, step=100.0, format="%.2f")

meses = ["Janeiro", "Fevereiro", "Março"]
indicadores = ["Produção", "Ticket Médio", "Despesas", "Satisfação Cliente", "Pesquisa Clima", "Turnover", "ABS", "Treinamento"]

# Criando os checkboxes em colunas
col1, col2, col3 = st.columns(3)

indicadores_vars = []

for i, col in enumerate([col1, col2, col3]):
    with col:
        st.subheader(meses[i])
        indicadores_mes = {}
        for indicador in indicadores:
            indicadores_mes[indicador] = st.checkbox(f"{indicador} ({meses[i]})", value=True)
        indicadores_vars.append(indicadores_mes)

if st.button("Calcular"):
    total_recebido = calcular_meta(valor_mensal, indicadores_vars)
    st.success(f"Valor final da meta trimestral: R$ {total_recebido:.2f}")
