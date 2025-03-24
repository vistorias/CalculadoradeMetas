import streamlit as st
import pandas as pd

# Configuração da página
st.set_page_config(page_title="Calculadora de Metas Trimestrais", layout="wide")
st.markdown("<h1 style='text-align: center;'>📊 Calculadora de Metas Trimestrais</h1>", unsafe_allow_html=True)

# Entrada de valor mensal
st.markdown("<h6>Digite o valor mensal da meta:</h6>", unsafe_allow_html=True)
valor_mensal = st.number_input("", min_value=0.0, step=10.0, format="%.2f")

# Pesos dos indicadores
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

meses = ["Janeiro", "Fevereiro", "Março"]
col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
colunas = [col1, col2, col3]

# Armazenar seleções
selecoes = {mes: {} for mes in meses}
resultado_individual = {indicador: {mes: True for mes in meses} for indicador in pesos}

# Criação dos checkboxes
for idx, mes in enumerate(meses):
    with colunas[idx]:
        st.subheader(mes)
        for indicador in pesos:
            chave = f"{indicador} ({mes})"
            selecionado = st.checkbox(chave, value=True)
            selecoes[mes][indicador] = selecionado
            resultado_individual[indicador][mes] = selecionado

# Coluna de valor bônus
with col4:
    st.subheader("Valor Bônus")
    for indicador in pesos:
        total = 0
        completo = True
        for mes in meses:
            if not resultado_individual[indicador][mes]:
                completo = False
            else:
                total += valor_mensal * pesos[indicador]

        if completo:
            st.markdown(f"✅ R$ {total:.2f}")
        else:
            st.markdown(f"❌ R$ {valor_mensal * pesos[indicador]:.2f}")

# Total perdido por mês
st.markdown("<hr>", unsafe_allow_html=True)
col_jan, col_fev, col_mar = st.columns(3)
total_perdido_mes = {}
for i, mes in enumerate(meses):
    total = 0
    for indicador in pesos:
        if not selecoes[mes][indicador]:
            total += valor_mensal * pesos[indicador]
    total_perdido_mes[mes] = total
    with [col_jan, col_fev, col_mar][i]:
        st.markdown(f"<div style='text-align: center; font-weight: bold;'>Total perdido em {mes}: <span style='color: red;'>R$ {total:.2f}</span></div>", unsafe_allow_html=True)

# Botão Calcular e resultado final
if st.button("Calcular"):
    total_trimestre = valor_mensal * 3
    total_perdido = sum(total_perdido_mes.values())
    valor_final = total_trimestre - total_perdido

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <div style='text-align: center; font-size: 20px; font-weight: bold;'>
        🧮 Total perdido no trimestre: <span style='color: red;'>R$ {:.2f}</span><br><br>
        ✅ Valor final da meta a receber: <span style='color: green;'>R$ {:.2f}</span>
    </div>
    """.format(total_perdido, valor_final), unsafe_allow_html=True)
